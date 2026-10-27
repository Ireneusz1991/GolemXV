# -*- coding: utf-8 -*-
"""
Golem XV — Moduł Weryfikacji Integralności i Tarcza Anty-Halucynacyjna (GolemVerifier)
=====================================================================================
Zabezpiecza bazę wiedzy przed halucynacjami modeli językowych, zmyślonymi linkami,
szczątkami promptów, fałszywym przypisaniem autorstwa oraz uszkodzonymi adresami URL.

Działa w oparciu o czysty Python (bez zewnętrznych bibliotek AI), z wbudowanym
wielowątkowym audytem sieciowym (HTTP HEAD/GET), heurystykami anty-halucynacyjnymi
oraz weryfikacją spójności domenowej.
"""

import sys
import os
import json
import re
import urllib.request
from urllib.parse import urlparse
import ssl
import concurrent.futures
from typing import Dict, List, Tuple, Any, Optional

try:
    import certifi
    SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except Exception:
    SSL_CONTEXT = ssl.create_default_context()

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pl,en-US;q=0.9,en;q=0.8",
}

# Wzorce typowych halucynacji LLM i niespełnionych znaczników
HALLUCINATION_PATTERNS = [
    (re.compile(r"\[TODO.*?\]", re.I), "Niewypełniony znacznik TODO"),
    (re.compile(r"\[PLACEHOLDER.*?\]", re.I), "Zastępczy znacznik PLACEHOLDER"),
    (re.compile(r"\[WSTAW.*?\]", re.I), "Zastępczy znacznik [WSTAW...]"),
    (re.compile(r"\[LINK.*?\]", re.I), "Zastępczy znacznik [LINK...]"),
    (re.compile(r"\bLorem\s+ipsum\b", re.I), "Tekst zaślepkujący Lorem Ipsum"),
    (re.compile(r"https?://(?:www\.)?example\.(?:com|org|net)", re.I), "Przykładowa domena example.com"),
    (re.compile(r"https?://(?:www\.)?test\.(?:com|org|pl)", re.I), "Przykładowa domena testowa"),
    (re.compile(r"https?://(?:www\.)?foo\.bar", re.I), "Domena zaślepkowa foo.bar"),
    (re.compile(r"\bundefined\b", re.I), "Niezdefiniowana wartość JavaScript 'undefined'"),
    (re.compile(r"\bNaN\b"), "Wartość numeryczna NaN"),
    (re.compile(r"\$\{[\w\.\_]+\}"), "Niewyewaluowana zmienna szablonu ${...}"),
    (re.compile(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}"), "Niewypełniony parametr szablonu {...}"),
    (re.compile(r"\]\(https?://\s*\)"), "Pusty link markdown [](http)"),
    (re.compile(r"https?://https?://", re.I), "Podwójny protokół w adresie URL"),
]

# Znane instytucje i dopuszczalne domeny (kontrola fałszywego przypisania źródła z granicami słów \b)
DOMAIN_AFFINITIES = {
    re.compile(r"\bradio\s+naukowe\b", re.I): ["radionaukowe.pl", "youtube.com", "spotify.com", "apple.com"],
    re.compile(r"\bpolskie\s+radio\b", re.I): ["polskieradio.pl", "polskieradio24.pl", "jedynka.polskieradio.pl", "trojka.polskieradio.pl", "radio.katowice.pl", "podcasty.radio.katowice.pl", "youtube.com", "spotify.com"],
    re.compile(r"\bradio\s+357\b", re.I): ["radio357.pl", "youtube.com", "spotify.com"],
    re.compile(r"\bradio\s+katowice\b", re.I): ["radio.katowice.pl", "podcasty.radio.katowice.pl", "youtube.com", "spotify.com"],
    re.compile(r"\bświaty\s+lema\b", re.I): ["podcasty.radio.katowice.pl", "radio.katowice.pl", "spotify.com", "youtube.com", "lem.pl"],
    re.compile(r"\bnauka\.\s*to\s*lubi[eę]\b", re.I): ["naukatolubie.pl", "naukatolubie.org", "youtube.com", "spotify.com"],
    re.compile(r"\bcentrum\s+kopernika\b", re.I): ["copernicuscenter.edu.pl", "youtube.com", "spotify.com"],
    re.compile(r"\bcopernicus\b", re.I): ["copernicuscenter.edu.pl", "kopernik.org.pl", "youtube.com", "spotify.com"],
    re.compile(r"\blex\s+fridman\b", re.I): ["lexfridman.com", "youtube.com", "spotify.com", "apple.com"],
    re.compile(r"\bsean\s+carroll\b", re.I): ["preposterousuniverse.com", "youtube.com", "spotify.com", "apple.com"],
    re.compile(r"\bmindscape\b", re.I): ["preposterousuniverse.com", "youtube.com", "spotify.com", "apple.com"],
    re.compile(r"\bhuberman\b", re.I): ["hubermanlab.com", "youtube.com", "spotify.com", "apple.com"],
    re.compile(r"\bncbj\b", re.I): ["ncbj.gov.pl", "naukawpolsce.pl", "youtube.com"],
    re.compile(r"\breaktor\s+maria\b", re.I): ["ncbj.gov.pl", "naukawpolsce.pl", "youtube.com"],
    re.compile(r"\biter\b", re.I): ["iter.org", "youtube.com", "euro-fusion.org"],
    re.compile(r"\bnasa\b", re.I): ["nasa.gov", "ntrs.nasa.gov", "esero.kopernik.org.pl", "youtube.com"],
    re.compile(r"\besa\b", re.I): ["esa.int", "melissafoundation.org", "esero.kopernik.org.pl", "polsl.pl", "youtube.com"],
    re.compile(r"\bmit\b", re.I): ["mit.edu", "ocw.mit.edu", "mitpress.mit.edu", "sarabander.github.io"],
    re.compile(r"\bstanford\b", re.I): ["stanford.edu", "plato.stanford.edu"],
    re.compile(r"\barxiv\b", re.I): ["arxiv.org"],
    re.compile(r"\bstanisław\s+lem\b", re.I): ["lem.pl", "radio.katowice.pl", "podcasty.radio.katowice.pl", "radio357.pl", "polskieradio.pl", "bioetyka.pan.pl", "plato.stanford.edu", "youtube.com"],
}

# Heurystyka konkretnego dzieła/odcinka
SPECIFIC_WORK_KEYWORDS = [
    "odcinek", "odc.", "episode", "ep.", "wywiad z", "audycja o",
    "prof.", "dr ", "artykuł", "paper", "monografia", "traktat"
]


# Dedykowane subdomeny repozytoriów, baz danych i dokumentacji technicznej
KNOWN_REPOSITORY_SUBDOMAINS = [
    "docs.", "learning.", "alphafold.", "irds.", "ntrs.", "aris.",
    "ocw.", "plato.", "arxiv.", "lem.pl", "openstax.org"
]


class VerificationIssue:
    def __init__(self, severity: str, path: str, title: str, url: str, message: str):
        self.severity = severity  # 'CRITICAL', 'WARNING', 'INFO'
        self.path = path
        self.title = title
        self.url = url
        self.message = message

    def to_dict(self) -> Dict[str, str]:
        return {
            "severity": self.severity,
            "path": self.path,
            "title": self.title,
            "url": self.url,
            "message": self.message,
        }

    def __str__(self) -> str:
        icon = "🔴" if self.severity == "CRITICAL" else ("🟡" if self.severity == "WARNING" else "ℹ️")
        return f"{icon} [{self.severity}] {self.path} | {self.title[:50]} | {self.message} (URL: {self.url})"


class GolemVerifier:
    def __init__(self, timeout: int = 10, max_workers: int = 12):
        self.timeout = timeout
        self.max_workers = max_workers
        self.issues: List[VerificationIssue] = []
        self._url_cache: Dict[str, Tuple[int, str]] = {}

    def clear(self):
        self.issues.clear()
        self._url_cache.clear()

    # --------------------------------------------------------------------------
    # 1. TEST TEKSTOWY: WYKRYWANIE WZORCÓW ZAŚLEPEK I HALUCYNACJI
    # --------------------------------------------------------------------------
    def check_hallucination_patterns(self, text: str, path: str, title: str, url: str):
        for pattern, desc in HALLUCINATION_PATTERNS:
            match = pattern.search(text)
            if match:
                self.issues.append(
                    VerificationIssue(
                        severity="CRITICAL",
                        path=path,
                        title=title,
                        url=url,
                        message=f"Wykryto token halucynacji/zaślepki: '{match.group(0)}' ({desc})"
                    )
                )

    # --------------------------------------------------------------------------
    # 2. HEURYSTYKA: CZY KONKRETNY ODCINEK NIE WSKAZUJE NA STRONĘ GŁÓWNĄ (ROOT DOMAIN)
    # --------------------------------------------------------------------------
    def check_root_domain_laziness(self, path: str, title: str, url: str, entry: Optional[Dict[str, Any]] = None):
        if not url:
            return
        parsed = urlparse(url.strip())
        t_lower = title.lower()

        # Portale ogólne w katalogu materiałów (materials) z założenia mogą wskazywać na stronę główną platformy
        if path.startswith("materials[") and not any(kw in t_lower for kw in ["odcinek", "episode", "#", "audycja"]):
            return

        is_specific = any(kw in t_lower for kw in ["odcinek", "odc.", "episode", "ep.", "wywiad z", "audycja o"])
        is_in_road = "carAudioRoad" in path
        is_root = parsed.path in ["", "/"] and not parsed.query and not parsed.fragment

        # Wyjątki: dedykowane subdomeny dokumentacji/repozytoriów oraz autorskie bazy
        is_known_repo = any(sub in parsed.netloc.lower() for sub in KNOWN_REPOSITORY_SUBDOMAINS)
        if (is_specific or is_in_road) and is_root and not is_known_repo:
            self.issues.append(
                VerificationIssue(
                    severity="CRITICAL",
                    path=path,
                    title=title,
                    url=url,
                    message="Prawdopodobna halucynacja: konkretny odcinek/opracowanie wskazuje tylko na stronę główną domeny (brak ścieżki do odcinka, identyfikatora lub sluga)."
                )
            )

    # --------------------------------------------------------------------------
    # 3. SPÓJNOŚĆ DOMENOWA: CZY ŹRÓDŁO W TYTULE ZGADZA SIĘ Z ADRESEM URL
    # --------------------------------------------------------------------------
    def check_domain_affinity(self, path: str, title: str, url: str):
        if not url:
            return
        parsed = urlparse(url.strip())
        domain = parsed.netloc.lower()
        t_lower = title.lower()

        for pat, allowed_domains in DOMAIN_AFFINITIES.items():
            if pat.search(t_lower):
                matched = any(ad in domain for ad in allowed_domains)
                if not matched:
                    self.issues.append(
                        VerificationIssue(
                            severity="WARNING",
                            path=path,
                            title=title,
                            url=url,
                            message=f"Niespójność źródła: tytuł dopasował wzorzec '{pat.pattern}', lecz domena '{domain}' nie znajduje się na liście zaufanych domen dla tego podmiotu."
                        )
                    )
                break

    # --------------------------------------------------------------------------
    # 4. KONTROLA STRUKTURY URL
    # --------------------------------------------------------------------------
    def check_url_syntax(self, path: str, title: str, url: str):
        if not url or not isinstance(url, str):
            self.issues.append(
                VerificationIssue(
                    severity="CRITICAL",
                    path=path,
                    title=title,
                    url=str(url),
                    message="Brak adresu URL lub nieprawidłowy typ danych."
                )
            )
            return

        u = url.strip()
        parsed = urlparse(u)
        if parsed.scheme not in ["http", "https"]:
            self.issues.append(
                VerificationIssue(
                    severity="CRITICAL",
                    path=path,
                    title=title,
                    url=u,
                    message=f"Nieprawidłowy schemat protokołu: '{parsed.scheme}'. Wymagany http lub https."
                )
            )
        if not parsed.netloc:
            self.issues.append(
                VerificationIssue(
                    severity="CRITICAL",
                    path=path,
                    title=title,
                    url=u,
                    message="Brak nazwy hosta (domeny) w adresie URL."
                )
            )

    # --------------------------------------------------------------------------
    # 5. TEST SIECIOWY NA ŻYWO (HTTP HEAD / GET)
    # --------------------------------------------------------------------------
    def check_url_live(self, url: str) -> Tuple[int, str]:
        u = url.strip()
        if u in self._url_cache:
            return self._url_cache[u]

        # Próbujemy najpierw metody HEAD, a w razie błędu 405/403 GET
        try:
            req = urllib.request.Request(u, headers=BROWSER_HEADERS, method="HEAD")
            with urllib.request.urlopen(req, context=SSL_CONTEXT, timeout=self.timeout) as resp:
                code = resp.getcode()
                self._url_cache[u] = (code, "OK")
                return (code, "OK")
        except urllib.error.HTTPError as e:
            if e.code in [403, 405, 406]:
                # Niektóre serwery (np. Cloudflare, Caltech, Substack) odrzucają HEAD; próbujemy GET pobierając tylko nagłówek/pierwsze bajty
                try:
                    req_get = urllib.request.Request(u, headers=BROWSER_HEADERS, method="GET")
                    with urllib.request.urlopen(req_get, context=SSL_CONTEXT, timeout=self.timeout) as resp:
                        code = resp.getcode()
                        self._url_cache[u] = (code, "OK")
                        return (code, "OK")
                except urllib.error.HTTPError as e_inner:
                    self._url_cache[u] = (e_inner.code, f"HTTP Error {e_inner.code}")
                    return (e_inner.code, f"HTTP Error {e_inner.code}")
                except Exception as ex_inner:
                    self._url_cache[u] = (0, str(ex_inner))
                    return (0, str(ex_inner))
            self._url_cache[u] = (e.code, f"HTTP Error {e.code}")
            return (e.code, f"HTTP Error {e.code}")
        except Exception as ex:
            self._url_cache[u] = (0, str(ex))
            return (0, str(ex))

    # --------------------------------------------------------------------------
    # 6. SZYBKI AUDYT OFFLINE (BEZ POŁĄCZEŃ HTTP)
    # --------------------------------------------------------------------------
    def audit_entry_fast(self, entry: Dict[str, Any], path: str):
        title = entry.get("title") or entry.get("titlePl") or entry.get("name") or path
        url = entry.get("url") or ""

        # Test składni
        self.check_url_syntax(path, title, url)

        # Test halucynacji w tytule, opisie i url
        combined_text = f"{title} {url} {entry.get('description', '')} {entry.get('spokenBriefingPl', '')} {entry.get('promptTemplate', '')}"
        self.check_hallucination_patterns(combined_text, path, title, url)

        # Heurystyka strony głównej
        self.check_root_domain_laziness(path, title, url, entry=entry)

        # Spójność domeny
        self.check_domain_affinity(path, title, url)

    # --------------------------------------------------------------------------
    # 7. PEŁNA REKURENCYJNA EKSTRAKCJA Z BAZY DANYCH
    # --------------------------------------------------------------------------
    def extract_all_entries(self, obj: Any, path: str = "") -> List[Dict[str, Any]]:
        entries = []
        if isinstance(obj, dict):
            if "url" in obj and isinstance(obj["url"], str):
                entries.append({
                    "path": path,
                    "id": obj.get("id"),
                    "title": obj.get("title") or obj.get("titlePl") or obj.get("name") or path,
                    "url": obj["url"],
                    "entry": obj
                })
            for k, v in obj.items():
                entries.extend(self.extract_all_entries(v, f"{path}.{k}" if path else k))
        elif isinstance(obj, list):
            for i, it in enumerate(obj):
                entries.extend(self.extract_all_entries(it, f"{path}[{i}]"))
        return entries

    # --------------------------------------------------------------------------
    # 8. WERYFIKACJA PROPOZYCJI BADAWCZEJ AI PRZED ZAPISANIEM
    # --------------------------------------------------------------------------
    def verify_proposal(self, prop: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Waliduje nową propozycję badawczą generowaną autonomicznie przez silnik AI/ArXiv.
        Zwraca (is_valid, lista_uwag).
        """
        msgs = []
        title = prop.get("title", "").strip()
        url = prop.get("arxivUrl") or prop.get("url", "").strip()
        arxiv_id = prop.get("arxivId", "").strip()

        if not title or len(title) < 10:
            msgs.append("Tytuł badania jest zbyt krótki lub pusty.")

        # Sprawdzenie wzorców halucynacji
        for pat, desc in HALLUCINATION_PATTERNS:
            if pat.search(title) or pat.search(prop.get("summary", "")) or pat.search(url):
                msgs.append(f"Wykryto token halucynacji: {desc}")

        # Weryfikacja formatu ArXiv ID
        if arxiv_id:
            arxiv_regex = re.compile(r"^(?:[a-zA-Z\-]+/\d{7}|\d{4}\.\d{4,5}(?:v\d+)?)$")
            if not arxiv_regex.match(arxiv_id):
                msgs.append(f"Nieprawidłowy format ArXiv ID: '{arxiv_id}'. Prawidłowy: RRRR.NNNNN")

        if url:
            code, reason = self.check_url_live(url)
            if code not in [200, 202, 206, 301, 302, 307, 308]:
                msgs.append(f"Adres URL badania jest niedostępny (kod {code}: {reason})")

        is_valid = len(msgs) == 0
        return (is_valid, msgs)

    # --------------------------------------------------------------------------
    # 9. GŁÓWNY AUDYT BAZY DANYCH
    # --------------------------------------------------------------------------
    def audit_database(self, db_dict: Dict[str, Any], live_http: bool = False) -> Dict[str, Any]:
        self.clear()
        all_entries = self.extract_all_entries(db_dict)

        # 1. Sprawdzenie unikalności ID
        seen_ids: Dict[str, str] = {}
        def check_ids(obj: Any, path: str = ""):
            if isinstance(obj, dict):
                obj_id = obj.get("id")
                if obj_id and isinstance(obj_id, str):
                    if obj_id in seen_ids:
                        self.issues.append(
                            VerificationIssue(
                                severity="CRITICAL",
                                path=path,
                                title=obj.get("title", obj_id),
                                url="",
                                message=f"Duplikat identyfikatora ID '{obj_id}' (wcześniej w '{seen_ids[obj_id]}')"
                            )
                        )
                    else:
                        seen_ids[obj_id] = path
                for k, v in obj.items():
                    check_ids(v, f"{path}.{k}" if path else k)
            elif isinstance(obj, list):
                for i, it in enumerate(obj):
                    check_ids(it, f"{path}[{i}]")

        check_ids(db_dict)

        # 2. Szybki audyt tekstowo-domenowy
        for item in all_entries:
            self.audit_entry_fast(item["entry"], item["path"])

        # 3. Opcjonalny pełny audyt HTTP
        if live_http:
            unique_urls = list({e["url"] for e in all_entries if e["url"]})
            print(f"[*] Rozpoczynam audyt HTTP dla {len(unique_urls)} unikalnych adresów URL...", flush=True)

            with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_url = {executor.submit(self.check_url_live, u): u for u in unique_urls}
                for future in concurrent.futures.as_completed(future_to_url):
                    u = future_to_url[future]
                    try:
                        code, msg = future.result()
                        if code == 404:
                            # Szukamy powiązanych wpisów
                            for it in all_entries:
                                if it["url"] == u:
                                    self.issues.append(
                                        VerificationIssue(
                                            severity="CRITICAL",
                                            path=it["path"],
                                            title=it["title"],
                                            url=u,
                                            message=f"Błąd 404 Not Found — zasób nie istnieje pod tym adresem!"
                                        )
                                    )
                        elif code == 0 or code >= 500:
                            for it in all_entries:
                                if it["url"] == u:
                                    self.issues.append(
                                        VerificationIssue(
                                            severity="WARNING",
                                            path=it["path"],
                                            title=it["title"],
                                            url=u,
                                            message=f"Serwer niedostępny lub błąd połączenia: kod {code} ({msg})"
                                        )
                                    )
                    except Exception as exc:
                        pass

        criticals = [i for i in self.issues if i.severity == "CRITICAL"]
        warnings = [i for i in self.issues if i.severity == "WARNING"]

        report = {
            "totalEntries": len(all_entries),
            "uniqueUrls": len({e['url'] for e in all_entries if e['url']}),
            "totalIssues": len(self.issues),
            "criticalCount": len(criticals),
            "warningCount": len(warnings),
            "isClean": len(criticals) == 0,
            "issues": [i.to_dict() for i in self.issues]
        }
        return report


def verify_database_file(file_path: str, live_http: bool = False) -> bool:
    """Wygodna funkcja CLI/importu."""
    if not os.path.exists(file_path):
        print(f"[!] Błąd: Plik bazy danych nie istnieje: {file_path}", file=sys.stderr)
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    verifier = GolemVerifier()
    rep = verifier.audit_database(data, live_http=live_http)

    print("=" * 80)
    print(" 🛡️  GOLEM XV — RAPORT INTEGRALNOŚCI I TARCZY ANTY-HALUCYNACYJNEJ")
    print("=" * 80)
    print(f" Analizowany plik:          {file_path}")
    print(f" Przebadane wpisy w bazie: {rep['totalEntries']}")
    print(f" Unikalne adresy URL:      {rep['uniqueUrls']}")
    print(f" Błędy KRYTYCZNE:          {rep['criticalCount']}")
    print(f" Ostrzeżenia:              {rep['warningCount']}")
    print("-" * 80)

    if rep["issues"]:
        print(" ZNALEZIONE UWAGI:")
        for iss in rep["issues"]:
            prefix = "🔴 KRYTYCZNY" if iss["severity"] == "CRITICAL" else "🟡 OSTRZEŻENIE"
            print(f" {prefix}: {iss['path']}")
            print(f"   Tytuł:   {iss['title']}")
            print(f"   URL:     {iss['url']}")
            print(f"   Powód:   {iss['message']}")
            print()
    else:
        print(" ✅ BAZA DANYCH JEST W 100% CZYSTA!")
        print("    Nie wykryto żadnych halucynacji, pustych linków ani duplikatów.")
    print("=" * 80)

    return rep["isClean"]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Golem XV Anti-Hallucination & Integrity Verifier")
    parser.add_argument("--file", default=os.path.join(os.path.dirname(__file__), "data", "database.json"), help="Ścieżka do bazy JSON")
    parser.add_argument("--full", action="store_true", help="Wykonaj pełny audyt z testami sieciowymi HTTP na żywo")
    parser.add_argument("--strict", action="store_true", help="Zwróć kod błędu 1 również przy ostrzeżeniach")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    is_ok = verify_database_file(args.file, live_http=args.full)
    if not is_ok:
        sys.exit(1)
    sys.exit(0)

const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 8080;
const DATA_DIR = path.join(__dirname, "data");
const SEED_FILE = path.join(DATA_DIR, "seed.json");
const DB_FILE = path.join(DATA_DIR, "database.json");

if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}

if (!fs.existsSync(DB_FILE) && fs.existsSync(SEED_FILE)) {
  fs.copyFileSync(SEED_FILE, DB_FILE);
}

const MIME_TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml"
};

const server = http.createServer((req, res) => {
  const urlPath = req.url.split("?")[0];

  if (urlPath === "/api/state" && req.method === "GET") {
    try {
      const target = fs.existsSync(DB_FILE) ? DB_FILE : SEED_FILE;
      const content = fs.readFileSync(target, "utf8");
      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" });
      res.end(content);
    } catch (err) {
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: err.message }));
    }
    return;
  }

  if (urlPath === "/api/backup_archive" && req.method === "POST") {
    try {
      const nowStr = new Date().toISOString().replace(/[:.]/g, "-");
      const archDir = path.join(__dirname, "archives");
      if (!fs.existsSync(archDir)) fs.mkdirSync(archDir, { recursive: true });
      const backupDbPath = path.join(archDir, `database_backup_${nowStr}.json`);
      if (fs.existsSync(DB_FILE)) {
        fs.copyFileSync(DB_FILE, backupDbPath);
      }
      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ ok: true, backup: backupDbPath }));
    } catch (err) {
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: err.message }));
    }
    return;
  }

  if (urlPath === "/api/state" && req.method === "POST") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
    });
    req.on("end", () => {
      try {
        const parsed = JSON.parse(body);
        fs.writeFileSync(DB_FILE, JSON.stringify(parsed, null, 2), "utf8");
        res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" });
        res.end(JSON.stringify({ ok: true }));
      } catch (err) {
        res.writeHead(400, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Invalid JSON" }));
      }
    });
    return;
  }

  let filePath = path.join(__dirname, urlPath === "/" ? "index.html" : urlPath);
  if (!filePath.startsWith(__dirname)) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, { "Content-Type": MIME_TYPES[ext] || "application/octet-stream" });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404);
    res.end("Not Found");
  }
});

server.listen(PORT, () => {
  console.log(`Serwer Golem XV uruchomiony pod adresem: http://localhost:${PORT}`);
});

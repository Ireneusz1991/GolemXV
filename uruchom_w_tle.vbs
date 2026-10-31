Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
strDir = fso.GetParentFolderName(WScript.ScriptFullName)

' Uruchomienie Watchdoga w tle bez okna konsoli (0 = ukryte)
WshShell.CurrentDirectory = strDir
WshShell.Run "python golem_watchdog.py", 0, False

# Test

Dieses Repository enthaelt ein kleines Beispiel einer modernen Benutzeroberflaeche im Apple-Stil.
Die Dateien befinden sich im Ordner `ui`:

- `index.html` - Startseite der Anwendung
- `style.css` - Gestaltung im macOS-Design
- `script.js` - Einfache Interaktion

Oeffnen Sie `index.html` in einem Browser unter Windows, um die Oberflaeche zu testen.

Weitere Beitraege und Review-Ablauf: siehe `CONTRIBUTING.md`.
Sicherheitsmeldungen: siehe `SECURITY.md`.
QA- und Regressionstests: siehe `QA_CHECKLIST.md`.

## QA und lokaler Test

Fuehren Sie im Repository aus:

```bash
npm test
```

Der Smoke-Test prueft, dass die zentralen UI-Dateien vorhanden sind und die Button-Interaktion verdrahtet ist.
Optionaler Browser-Smoketest:

```bash
npm run test:e2e
```

Im CI laufen E2E-Tests mit Retry- und Trace-Unterstuetzung fuer stabilere Diagnose bei Flakes.

Zusätzlicher Qualitaetscheck:

```bash
npm run lint
```

Zusätzlich läuft dieser Test automatisch per GitHub Actions bei Pushes und Pull Requests.

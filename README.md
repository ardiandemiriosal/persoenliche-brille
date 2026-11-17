# Persönliche Brille

Gemeinsamer Agent Skill für Claude Code und Codex. Er beschreibt, wie ein privates persönliches Profil gelesen, zweckabhängig angewendet und mit ausdrücklichen Nutzerkorrekturen gepflegt wird.

Dieses Repository enthält kein persönliches Profil. Jede Person verwendet ihre eigene lokale Datei. Altin, Florian und andere können dieselbe Anleitung mit ihrem eigenen Profil nutzen.

## Installieren

Repository klonen, dann:

```sh
python3 scripts/install.py --profile /absoluter/pfad/zum/eigenen-profil.md
```

Der Installer verknüpft denselben Skillordner unter `~/.agents/skills/persoenliche-brille` (Codex) und `~/.claude/skills/persoenliche-brille` (Claude Code). Er schreibt die private Pfadkonfiguration nach `~/.config/persoenliche-brille/config.json`. Vorhandene abweichende Installationen werden nicht überschrieben.

Neue Sitzungen verwenden den installierten Skill nach Auswahl durch den Agenten oder explizit als `$persoenliche-brille` (Codex) beziehungsweise `/persoenliche-brille` (Claude Code). Für Anwendung bei jedem Projektstart in die jeweilige AGENTS.md oder CLAUDE.md aufnehmen:

> Lies zu Sitzungsbeginn den installierten Skill persoenliche-brille und das darin konfigurierte private Profil. Berücksichtige bestätigte Präferenzen und pflege neue ausdrückliche Wünsche gemäss Skill.

Ein Skill verleiht keine Dateirechte. Profil-Lesen und -Schreiben müssen für das jeweilige Werkzeug erlaubt sein. Normale Browserchats werden durch die lokale Installation nicht verbunden.

## Gemeinsame Pflege

Vor Änderungen `git pull --ff-only`. Nur öffentliche, generische oder synthetische Beispiele verwenden. Keine privaten Profile oder Chats als Input einer Veröffentlichung verwenden. Nach Änderungen `python3 scripts/validate.py`, Diff prüfen, gezielt committen und ohne Force-Push veröffentlichen. Bei Konflikten stoppen und zusammenführen lassen.

Der geplante lokale Tageslauf prüft nacheinander mit Claude Code und Codex, damit beide den gleichen integrierten Stand sehen. Ein Lauf ohne begründete Änderung erzeugt keinen Commit. Änderungen anderer Beteiligter werden vor und nach der Bearbeitung integriert. Der Mac und die benötigten Anmeldungen müssen verfügbar sein; eine Uhrzeit garantiert kein Aufwecken eines ausgeschalteten Rechners.

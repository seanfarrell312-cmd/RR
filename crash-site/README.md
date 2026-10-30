# Crash Team

Live: https://crashteam.redguygreenguy.com (deploys automatically from `main`).

A browser RTS / automation game about a crashed starship's robot crew. Open `crash-site.html` in a browser to play.

- Design decisions: `docs/DESIGN_LOG.md`
- Next planned update: `docs/FEATURE_SPEC_next.md`
- Instructions for Claude Code: `CLAUDE.md`
- Regression test: `python tests/playthrough.py` (needs `pip install playwright` and `python -m playwright install chromium` once)

## Working with Claude Code and Git

1. Install Git (https://git-scm.com/downloads). On Windows, Git for Windows is recommended for Claude Code.
2. Install Claude Code (needs a paid Claude plan):
   - macOS, Linux, WSL: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
   - Check it: `claude --version`. If something's wrong, `claude doctor`.
3. Put this folder somewhere permanent, open a terminal in it, and run:
   ```
   git init
   git add .
   git commit -m "Initial import: level 1 playable, design log, next-update spec"
   ```
4. Start Claude Code in the same folder: `claude`. Sign in when the browser opens. Claude Code reads `CLAUDE.md` automatically and can run git itself (commits, branches, diffs, reverting).
5. Optional, for an off-machine backup and history on the web: create an empty repository on GitHub (no README), then
   ```
   git remote add origin https://github.com/YOUR-NAME/crash-site.git
   git branch -M main
   git push -u origin main
   ```
   After that, ask Claude Code to push when you want a backup.

Suggested first prompt in Claude Code: "Read CLAUDE.md and the docs folder, run the playthrough test, then walk me through the open questions in docs/FEATURE_SPEC_next.md."

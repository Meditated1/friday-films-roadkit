#!/bin/bash
# FryDay Films Road Atlas — one-click push to GitHub
cd "$(dirname "$0")" || exit 1
echo "🚛  FryDay Films Road Atlas — pushing to GitHub"
echo "📂  $(pwd)"
echo

if [ ! -d ".git" ]; then
  echo "⚠️  This folder isn't a git repo yet."
  echo "    First-time setup (do once):"
  echo "      git init && git add . && git commit -m \"FryDay Films Road Atlas\""
  echo "      git branch -M main"
  echo "      git remote add origin https://github.com/YOUR-USERNAME/friday-films-roadkit.git"
  echo "      git push -u origin main"
  echo
  echo "Press any key to close…"; read -n 1 -s; exit 1
fi

git add -A
if git diff --cached --quiet; then
  echo "✅  Nothing new — GitHub is already up to date."
else
  git commit -m "Update $(date '+%Y-%m-%d %H:%M')" && git push && \
  echo && echo "✅  Pushed!  Give GitHub Pages ~1 min, then hard-refresh your site (Cmd+Shift+R)." || \
  echo "❌  Push failed — check your internet / GitHub login and try again."
fi
echo
echo "Press any key to close…"; read -n 1 -s

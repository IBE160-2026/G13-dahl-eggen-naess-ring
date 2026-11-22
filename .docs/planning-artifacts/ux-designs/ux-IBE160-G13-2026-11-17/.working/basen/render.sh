#!/bin/sh
# Rendrer skjermer/*.svg til png/ med Edge headless. Bruk: sh render.sh [navn ...]
E="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
mkdir -p png
P=$(cygpath -w "$PWD")
for f in skjermer/*.svg; do
  n=$(basename "$f" .svg)
  if [ $# -gt 0 ]; then case " $* " in *" ${n%%-*} "*) ;; *) continue;; esac; fi
  "$E" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 --screenshot="$P/png/$n.png" --window-size=390,844 "file:///$P/skjermer/$n.svg" 2>/dev/null
done

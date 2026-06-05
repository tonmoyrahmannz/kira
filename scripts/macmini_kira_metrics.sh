#!/bin/zsh
metric="$1"
case "$metric" in
  cpu)
    top -l 1 | perl -ne 'if(/CPU usage: .*?, .*?,\s*([0-9.]+)% idle/){printf "%.1f\n",100-$1; exit}'
    ;;
  memory)
    top -l 1 | perl -ne 'if(/PhysMem: ([0-9.]+)([MG]) used.*?, ([0-9.]+)([MG]) unused/){$u=$1*($2 eq q(G)?1024:1);$f=$3*($4 eq q(G)?1024:1);printf "%.1f\n",100*$u/($u+$f); exit}'
    ;;
  storage)
    df -k / | awk 'NR==2{gsub(/%/,"",$5); print $5}'
    ;;
  gpu)
    # Lightweight fallback. Replace with iStats/pmset-based metric later if desired.
    echo 0
    ;;
  nas_total)
    df -k /Volumes/Plex_HD | awk 'NR==2{gsub(/%/,"",$5); print $5}'
    ;;
  nas_online)
    if [ -d /Volumes/Plex_HD ]; then echo ON; else echo OFF; fi
    ;;
  nas_media)
    python3 - <<'PY'
import subprocess
def duk(path):
    try:return float(subprocess.check_output(['du','-sk',path],stderr=subprocess.DEVNULL,text=True).split()[0])
    except:return 0.0
T=duk('/Volumes/Plex_HD'); C=duk('/Volumes/Plex_HD/Media')
print(f"{(C/T*100 if T else 0):.1f}")
PY
    ;;
  nas_documents)
    python3 - <<'PY'
import subprocess
def duk(path):
    try:return float(subprocess.check_output(['du','-sk',path],stderr=subprocess.DEVNULL,text=True).split()[0])
    except:return 0.0
T=duk('/Volumes/Plex_HD'); C=duk('/Volumes/Plex_HD/Documents')
print(f"{(C/T*100 if T else 0):.1f}")
PY
    ;;
  nas_backups)
    python3 - <<'PY'
import subprocess
def duk(path):
    try:return float(subprocess.check_output(['du','-sk',path],stderr=subprocess.DEVNULL,text=True).split()[0])
    except:return 0.0
T=duk('/Volumes/Plex_HD'); C=duk('/Volumes/Plex_HD/Backups')
print(f"{(C/T*100 if T else 0):.1f}")
PY
    ;;
  nas_archive)
    python3 - <<'PY'
import subprocess
def duk(path):
    try:return float(subprocess.check_output(['du','-sk',path],stderr=subprocess.DEVNULL,text=True).split()[0])
    except:return 0.0
T=duk('/Volumes/Plex_HD'); C=duk('/Volumes/Plex_HD/Archive')
print(f"{(C/T*100 if T else 0):.1f}")
PY
    ;;
  *)
    echo unknown
    ;;
esac

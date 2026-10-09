"""Create the hackathon source ZIP from tracked files, never dependencies/secrets."""
from pathlib import Path
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
target = root / 'artifacts' / 'Sahi-GST-source.zip'
target.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in files:
        if name and (root / name).is_file():
            if name.startswith('.env') and name != '.env.example': raise RuntimeError('Secret environment file is tracked; stop packaging.')
            archive.write(root / name, 'Sahi-GST/' + name)
size = target.stat().st_size
if size >= 10_000_000: raise RuntimeError(f'ZIP exceeds the 10 MB limit: {size} bytes')
print(f'{target}\n{size} bytes — below 10 MB')

"""Build the real Next.js frontend and migrate the connected PostgreSQL DB."""
import subprocess
import os
from pathlib import Path
root = Path(__file__).resolve().parents[1]
npm = 'npm.cmd' if os.name == 'nt' else 'npm'
subprocess.run([npm, 'ci', '--prefix', 'frontend', '--no-audit', '--no-fund'], cwd=root, check=True)
subprocess.run([npm, 'run', 'build', '--prefix', 'frontend'], cwd=root, check=True)
subprocess.run(['python', 'manage.py', 'migrate', '--noinput'], cwd=root, check=True)

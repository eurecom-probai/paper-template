#!/usr/bin/env python
"""Post-generation hook to flatten project structure to selected conference."""

import os
import shutil
import re
from pathlib import Path

# Get the conference slug from cookiecutter context
conference_slug = "{{ cookiecutter.conference_slug }}"
conference_name = "{{ cookiecutter.conference }}"
project_root = Path.cwd()

print(f"📦 Restructuring project for {conference_slug.upper()}...")

# Paths
conferences_dir = project_root / "conferences"
selected_conf_dir = conferences_dir / conference_slug
commons_dir = project_root / "commons"
target_dir = project_root / conference_slug

# Step 1: Create conference subdirectory
print(f"📁 Creating {conference_slug}/ directory...")
target_dir.mkdir(exist_ok=True)
print(f"  ✓ Created {conference_slug}/")

# Step 2: Move commons files to conference directory
print(f"📁 Moving commons files to {conference_slug}/...")
if commons_dir.exists():
    for item in commons_dir.iterdir():
        dest = target_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest)
            # Make shell scripts executable
            if item.suffix == ".sh":
                os.chmod(dest, 0o755)
        print(f"  ✓ {item.name}")

# Step 3: Move selected conference files to conference directory
print(f"📄 Moving {conference_slug} conference files to {conference_slug}/...")
if selected_conf_dir.exists():
    for item in selected_conf_dir.iterdir():
        dest = target_dir / item.name
        shutil.copy2(item, dest)
        print(f"  ✓ {item.name}")

# Step 4: Update main.tex to remove ../../commons/ paths
main_tex = target_dir / "main.tex"
if main_tex.exists():
    print("🔧 Updating paths in main.tex...")
    content = main_tex.read_text()
    content = content.replace("../../commons/", "")
    main_tex.write_text(content)
    print("  ✓ Updated relative paths")

# Step 5: Clean up directories
print("🧹 Cleaning up template directories...")
if conferences_dir.exists():
    shutil.rmtree(conferences_dir)
    print("  ✓ Removed conferences/")

if commons_dir.exists():
    shutil.rmtree(commons_dir)
    print("  ✓ Removed commons/")

print(f"\n✅ Project restructured successfully for {conference_name}!")
print(f"   All files are now in {conference_slug}/ directory.")

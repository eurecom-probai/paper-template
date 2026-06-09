# 📄 Academic Paper Template

![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A cookiecutter template for academic papers with pre-configured setups for major ML conferences (ICML, ICLR, TMLR, UAI).

## ✨ Features

- 🎯 **Multi-Conference Support** — Ready-to-use templates for ICML, ICLR, TMLR, and UAI
- 📚 **Organized Structure** — Common bibliography, custom math commands, and shared content
- 🔧 **Automated Setup** — Post-generation hooks for seamless initialization
- 🧹 **Clean BibTeX** — Included script to sanitize bibliography entries

## 🚀 Quick Start

### Using uvx (Recommended)

```bash
uvx cookiecutter gh:eurecom-probai/paper-template
```

Or from a local directory:

```bash
uvx cookiecutter /path/to/paper-template
```

### Using pip-installed cookiecutter

```bash
pip install cookiecutter
cookiecutter gh:eurecom-probai/paper-template
```

### Adding a Conference to Existing Project

⚠️ **Use at your own risk** — This will overwrite existing files!

```bash
cd your-paper
uvx cookiecutter /path/to/paper-template --overwrite-if-exists
```

This allows you to add or switch conference templates in an existing project. The `--overwrite-if-exists` flag will potentially replace files with the same name if you choose the same conference multiple times. **Always commit your changes to git before running this command.**

## 📋 Configuration

During setup, you'll be prompted for:

- **project_slug** — Directory name for your paper (e.g., `my-awesome-paper`)

## 📁 Template Structure

```
paper-template/
├── cookiecutter.json
├── {{cookiecutter.project_slug}}/
│   ├── commons/
│   │   ├── clean-bibtex.sh
│   │   ├── math_commands.sty
│   │   ├── references.bib
│   │   ├── config/
│   │   │   ├── acronyms.tex
│   │   │   └── packages.tex
│   │   └── content/
│   │       └── 0_introduction.tex
│   └── conferences/
│       ├── icml/
│       ├── iclr/
│       ├── tmlr/
│       └── uai/
└── hooks/
    └── post_gen_project.py
```

### Generated Project Structure

After running cookiecutter, your project will have:

```
your-paper/
└── iclr/                      # Conference-specific directory
    ├── main.tex                   # Main LaTeX file
    ├── math_commands.sty          # Custom math macros
    ├── references.bib             # Bibliography
    ├── clean-bibtex.sh            # BibTeX cleanup script
    ├── iclr2026_conference.sty    # Conference-specific style files
    ├── iclr2026_conference.bst    # (depends on chosen conference)
    ├── config/
    │   ├── acronyms.tex           # Acronym definitions
    │   └── packages.tex           # Common LaTeX packages
    └── content/
        └── 0_introduction.tex     # Paper sections
```

## 🔨 Usage

1. **Navigate to conference directory** — `cd your-paper/iclr/` (or your chosen conference)
2. **Edit content** — Write your paper sections in `content/` directory
3. **Add references** — Update `references.bib` with your citations
4. **Compile** — Run `pdflatex main.tex` or use your preferred LaTeX editor
5. **Clean bibliography** — Run `./clean-bibtex.sh` when needed

## 💡 Tips

- The post-generation hook creates a conference-specific subdirectory for your chosen venue
- Custom math commands are defined in `math_commands.sty`
- Add acronyms to `config/acronyms.tex` for automatic expansion
- Organize your paper sections in the `content/` directory

## 📝 Requirements

- LaTeX distribution (TeX Live, MiKTeX, etc.)
- Python 3.8+ (for cookiecutter)

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📜 License

MIT License — See LICENSE file for details.

---

**Happy Writing! 🎓**

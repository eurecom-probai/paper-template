# 📄 Academic Paper Template

![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A cookiecutter template for academic papers with pre-configured setups for major ML conferences (ICML, NeurIPS, UAI).

## ✨ Features

- 🎯 **Multi-Conference Support** — Ready-to-use templates for ICML, NeurIPS, and UAI
- 📚 **Organized Structure** — Common bibliography, custom math commands, and shared content
- 🔧 **Automated Setup** — Post-generation hooks for seamless initialization
- 🧹 **Clean BibTeX** — Included script to sanitize bibliography entries

## 🚀 Quick Start

### Using uvx (Recommended)

```bash
uvx cookiecutter gh:yourusername/paper-template
```

Or from a local directory:

```bash
uvx cookiecutter /path/to/paper-template
```

### Using pip-installed cookiecutter

```bash
pip install cookiecutter
cookiecutter gh:yourusername/paper-template
```

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
│       ├── neurips/
│       └── uai/
└── hooks/
    └── post_gen_project.py
```

### Generated Project Structure

After running cookiecutter, your project will have:

```
your-paper/
├── main.tex                   # Main LaTeX file
├── math_commands.sty          # Custom math macros
├── references.bib             # Bibliography
├── clean-bibtex.sh            # BibTeX cleanup script
├── icml2026.sty               # Conference-specific style files
├── icml2026.bst               # (depends on chosen conference)
├── config/
│   ├── acronyms.tex           # Acronym definitions
│   └── packages.tex           # Common LaTeX packages
└── content/
    └── 0_introduction.tex     # Paper sections
```

## 🔨 Usage

1. **Edit content** — Write your paper sections in `content/` directory
2. **Add references** — Update `references.bib` with your citations
3. **Compile** — Run `pdflatex main.tex` or use your preferred LaTeX editor
4. **Clean bibliography** — Run `./clean-bibtex.sh` when needed

## 💡 Tips

- The post-generation hook flattens the structure and copies conference-specific files
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

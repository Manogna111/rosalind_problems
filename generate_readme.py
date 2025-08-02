import os
from pathlib import Path

# Set the path to your Rosalind problems folder
rosalind_dir = Path("rosalind")  # Change this if your folder is elsewhere

# Create the folder if it doesn't exist
rosalind_dir.mkdir(parents=True, exist_ok=True)

# Get all .py files
problem_files = sorted(rosalind_dir.glob("*.py"))

# Create the markdown list of problems
problem_entries = [
    f"- [{file.stem}](./{file.relative_to(rosalind_dir.parent)})"
    for file in problem_files
]

problem_list_md = "\n".join(problem_entries)

# Create the README content
readme_content = f"""# 🧬 Rosalind Bioinformatics Problems

This repository contains my solutions to the problems on [Rosalind](https://rosalind.info), a platform for learning bioinformatics through programming.

---

## 📁 Problem List

{problem_list_md}

---

## 🧪 How to Run

Run an individual script:

```bash
python <filename>.py

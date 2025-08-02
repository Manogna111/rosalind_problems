from pathlib import Path

# Set your Rosalind directory
rosalind_dir = Path("rosalind")  # Change if it's in a different location

# Make sure it exists
rosalind_dir.mkdir(parents=True, exist_ok=True)

# Gather all .py files
problem_files = sorted(rosalind_dir.glob("*.py"))

# Generate the markdown list
problem_entries = [
    f"- [{file.stem}](./{file.relative_to(rosalind_dir.parent)})"
    for file in problem_files
]

problem_list_md = "\n".join(problem_entries)

# Construct README without using f-strings inside triple quotes
readme_content = (
    "# 🧬 Rosalind Bioinformatics Problems\n\n"
    "This repository contains my solutions to the problems on [Rosalind](https://rosalind.info), "
    "a platform for learning bioinformatics through programming.\n\n"
    "---\n\n"
    "## 📁 Problem List\n\n"
    f"{problem_list_md}\n\n"
    "---\n\n"
    "## 🧪 How to Run\n\n"
    "Run an individual script:\n\n"
    "```bash\n"
    "python <filename>.py\n"
    "```\n\n"
    "---\n\n"
    "## 🧠 About Rosalind\n\n"
    "Rosalind problems help reinforce concepts in:\n"
    "- DNA/RNA manipulation\n"
    "- Genetics and inheritance\n"
    "- Bioinformatics algorithms\n"
    "- Combinatorics and graph theory\n\n"
    "---\n\n"
    "## 🔧 Environment\n\n"
    "- Language: Python 3\n"
    "- Dependencies: None (standard libraries only unless specified)\n\n"
    "---\n\n"
    "> “Rosalind is to bioinformatics what LeetCode is to software engineering.”\n"
)

# Save to README.md
readme_path = rosalind_dir / "README.md"
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"✅ README.md created at: {readme_path.resolve()}")

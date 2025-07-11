import re
from fileinput import filename
from typing import List

from bs4 import BeautifulSoup
import textwrap
import json
import subprocess


def github_commit(file_name, s):
    filename = file_name  # Replace with your actual file
    commit_message = f"Add {s}"
    branch = "main"  # Change to your branch name if needed

    try:
        # Add the file to staging
        subprocess.run(["git", "add", filename], check=True)

        # Commit the file
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to remote
        subprocess.run(["git", "push", "origin", branch], check=True)

        print("✅ File pushed to GitHub successfully.")

    except subprocess.CalledProcessError as e:
        print("❌ Git command failed:", e)

def get_description(s) -> str:
    desc_match = re.split(r'\n+Example \d+:', s)[0].strip()

    # Extract constraints
    constraints_match = re.search(r'Constraints:\s*(.+?)(?=\n\n|Follow up:)', s, re.DOTALL)
    constraints = constraints_match.group(0).strip() if constraints_match else ""

    # Extract follow-up
    follow_up_match = re.search(r'Follow up:.*', s)
    follow_up = follow_up_match.group(0).strip() if follow_up_match else ""

    # Combine into single `desc` variable
    desc = f"{desc_match}\n\n{constraints}\n\n{follow_up}"


    return  desc

def get_examples(s) ->  list[dict[str, str]]:
    # Regex to extract example blocks
    pattern = re.compile(
        r"Example\s*\d*:\s*\n*"
        r"Input:\s*(.*?)\n"
        r"Output:\s*(.*?)\n"
        r"(Explanation:\s*(.*?))?(?=\nExample|\nConstraints:|\Z)",
        re.DOTALL
    )

    matches = pattern.findall(s)

    # Clean and format the results
    examples = []
    for match in matches:
        input_text = match[0].strip()
        output_text = match[1].strip()
        explanation_text = match[3].strip() if match[2] else ""
        examples.append({
            "input": input_text,
            "output": output_text,
            "explanation": explanation_text
        })

    return  examples


# Read JSON from file
with open("payload.json", "r", encoding="utf-8") as f:
    data = json.load(f)

payload = data["data"]["question"]
python_snippet = next( (item["code"] for item in payload["codeSnippets"] if item["langSlug"] == "python3"), None )

print(payload["title"])

soup = BeautifulSoup(payload["content"], "html.parser")
cleaned = soup.get_text()

description = get_description(cleaned)
examples = get_examples(cleaned)

code_lines = python_snippet.splitlines()
new_snippet = []
func_name = "example"
if "List[" in python_snippet:
    new_snippet.append("from typing import List\n")
for line in code_lines:
    if not "class Solution" in line:
        if "def" in line:
            line = textwrap.dedent(line)
            match = re.search(r'def\s+(\w+)\s*\(', line)

            if match:
                func_name = match.group(1)
                print("Function name:", func_name)
            else:
                print("No function name found.")

        if "self" in line:
            line = re.sub(r'\bself,\s*', '', line)
            new_snippet.append(line)

# add desc
new_snippet.append("\t\"\"\"")
new_snippet.append(f"\t{payload["title"]}")
d = description.split("\n")
for line in d:
    if not line == "\n":
        new_snippet.append("\t" + line)
new_snippet.append("\t\"\"\"")
new_snippet.append("\tpass")
new_snippet.append("\n")

# add tests
for i, ex in enumerate(examples, 1):
    new_snippet.append(f"def test_example_{i}():")
    new_snippet.append("\t\"\"\"")
    new_snippet.append("\t" + f"Example {i}:")
    new_snippet.append("\t" + "Input:" + ex["input"])
    new_snippet.append("\t" + "Output:" + ex["output"])
    new_snippet.append("\t" + "Explanation:" + ex["explanation"])
    new_snippet.append("\t\"\"\"")
    new_snippet.append("\tpass")
    new_snippet.append("\n")


code = "\n".join(new_snippet)

output_file = f"Templates/{func_name}_template.py"

with open(output_file, "w") as f:
    f.write(code)

github_commit(output_file, payload["questionId"] + " " + payload["title"])
import re
from bs4 import BeautifulSoup
import textwrap
import subprocess
import requests


def github_commit(file_name, s):
    filename = file_name  # Replace with your actual file
    commit_message = f"Created  {s}"
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

def get_question_info(title_slug):
        url = "https://leetcode.com/graphql"
        session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJhY2NvdW50X3VzZXIiOiJheDF0ZiIsIl9hdXRoX3VzZXJfaWQiOiIxODMzODE2MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVjYTBkZmMzZDcyOTExYzFlN2U5MjM3YzY3M2EyMmI3YjQyZGQ5YzU2NTY0YmNhODE5NzVkYzdhY2M0NWNjNWQiLCJzZXNzaW9uX3V1aWQiOiJmM2M0OTgyNyIsImlkIjoxODMzODE2MywiZW1haWwiOiJ5dWxkdXouY2FsaWZvcm5pYUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImVsaXNhZ2F0ZXMiLCJ1c2VyX3NsdWciOiJlbGlzYWdhdGVzIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTc1MjI1NzkxMywiaXAiOiI1MC4xNjguNTQuMjIiLCJpZGVudGl0eSI6ImNlNjliODUxYzRlZGM3ZWViZmIzOTk4YWE5NGE3MTU3IiwiZGV2aWNlX3dpdGhfaXAiOlsiNTAxZGMwOTcxZGUxYTIwNjUyZjkzMzgzZmY3YmMxNjIiLCI1MC4xNjguNTQuMjIiXX0.MOQ75TDj1DqR5M1ku5idCBcBtOqidkz5HMjvv874FBg"

        token = "DJn0HRdmqjvZMk8WsI3ilc3yum73VXOB5dgo8wS8RNt8zYZeAzUYbQ9QYQ4j9M7a"
        headers = {
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/problems/{title_slug}/",
            f"Cookie": f"LEETCODE_SESSION={session}; csrftoken={token}",
            f"x-csrftoken": f"{token}",
            "User-Agent": "Mozilla/5.0"
        }

        payload = {
            "operationName": "questionData",
            "variables": {"titleSlug": title_slug},
            "query": """
            query questionData($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                questionId
                title
                difficulty
                content
                codeSnippets {
                  langSlug
                  code
                }
              }
            }
            """
        }
        response = requests.post(url, json=payload, headers=headers)

        return response.json()


slug = "remove-duplicates-from-sorted-array"
data = get_question_info(slug)
payload = data["data"]["question"]
python_snippet = next( (item["code"] for item in payload["codeSnippets"] if item["langSlug"] == "python3"), None )
soup = BeautifulSoup(payload["content"], "html.parser")
cleaned = soup.get_text()

description = get_description(cleaned)
examples = get_examples(cleaned)

code_lines = python_snippet.splitlines()
new_snippet = []
func_name = re.sub(r'-', '_', slug)
if "List[" in python_snippet:
    new_snippet.append("from typing import List\n")
for line in code_lines:
    if not "class Solution" in line:
        if "def" in line:
            line = textwrap.dedent(line)
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
    new_snippet.append(f"def test_{func_name}_example_{i}():")
    new_snippet.append("\t\"\"\"")
    new_snippet.append("\t" + f"Example {i}:")
    new_snippet.append("\t" + "Input:" + ex["input"])
    new_snippet.append("\t" + "Output:" + ex["output"])
    new_snippet.append("\t" + "Explanation:" + ex["explanation"])
    new_snippet.append("\t\"\"\"")
    new_snippet.append("\tpass")
    new_snippet.append("\n")


code = "\n".join(new_snippet)

output_file = f"TopInterview150/{func_name}_template.py"

with open(output_file, "w") as f:
    f.write(code)

github_commit(output_file, f"{payload["questionId"]}:  {payload["title"]}")
from bs4 import BeautifulSoup
import requests

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

    print("============")
    print(f"payload {response.content}")

    output_file = "payload.json"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.content.decode("utf-8"))

    return response.json()["data"]["question"]

def parse_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove code blocks to avoid capturing them in the description
    for tag in soup.find_all("pre"):
        tag.decompose()

    # 1. Get the clean description text (without examples or tags)
    paragraphs = soup.find_all(["p", "ul", "ol"])
    description_parts = []
    for p in paragraphs:
        if "example" in p.text.lower():
            break
        description_parts.append(p.get_text(separator=" ", strip=True))
    var1 = "\n".join(description_parts)

    # 2. Extract all example blocks (usually in <pre> tags)
    examples = []
    for tag in soup.find_all("pre"):
        example_text = tag.get_text(strip=True)
        if "example" in example_text.lower():
            examples.append(example_text)

    return var1, examples

# Example usage
slug = "merge-sorted-array"
question = get_question_info(slug)

var1, examples = parse_content(question["content"])

print("📄 Description:\n", var1)
print("\n🧪 Examples:")
for ex in examples:
    print("-", ex)

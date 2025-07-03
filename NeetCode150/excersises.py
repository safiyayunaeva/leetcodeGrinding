import requests

s = "AAAAAAA"

s1 = s.lower()
def download_leetcode_description(url, save_to=None):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text

        if save_to:
            with open(save_to, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Saved HTML to {save_to}")
        else:
            print(html[:500])  # preview first 500 chars
        return html

    except requests.RequestException as e:
        print(f"Error downloading page: {e}")
        return None

if __name__ == "__main__":
    url = "https://leetcode.com/problems/valid-anagram/description/"
    download_leetcode_description(url, save_to="valid_anagram.html")

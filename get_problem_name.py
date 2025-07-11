def read_first_line(file_name="urls.txt"):
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[0].strip() if lines else None

def remove_first_line(file_name="urls.txt"):
    with open(file_name, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(lines[1:])  # write all but the first
        f.truncate()

# Example usage
file_name = "urls.txt"
url = read_first_line(file_name)

if url:
    try:
        print("Processing:", url)
        # ▶️ Your action here (e.g., visit with Playwright, parse, etc.)
        success = False  # Replace with your actual success check

        if success:
            remove_first_line(file_name)
            print("✅ Success — line removed")
        else:
            print("⚠️ Not successful — line kept")

    except Exception as e:
        print(f"❌ Error processing {url}: {e}")
else:
    print("📭 File is empty")

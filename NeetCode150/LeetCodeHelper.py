import csv

def read_job_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category = row.get('Category')
                name = row.get('Name')
                status = row.get('Status')
                link = row.get('Link')
                notes = row.get('Notes')

                print(f"Category: {category}")
                print(f"Name: {name}")
                print(f"Status: {status}")
                print(f"Link: {link}")
                print(f"Notes: {notes}")
                print("-" * 40)

    except Exception as e:
        print(f"Error reading CSV: {e}")

# Example usage
read_job_csv("NeetCode150.csv")

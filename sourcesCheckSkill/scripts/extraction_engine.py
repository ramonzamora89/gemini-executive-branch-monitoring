import csv
import json
import os
import hashlib
from datetime import datetime

class ExtractionEngine:
    def __init__(self, output_dir=None):
        if output_dir is None:
            # Use absolute path relative to this script's location (up two levels)
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            self.output_dir = os.path.join(base_dir, "outputs")
        else:
            self.output_dir = output_dir
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            
        self.latest_csv = os.path.join(self.output_dir, "latest_posts.csv")
        self.archive_csv = os.path.join(self.output_dir, "posts_archive.csv")
        self.latest_json = os.path.join(self.output_dir, "latest_posts.json")
        self.headers = ["post_id", "account", "platform", "date", "content", "url", "topics", "sentiment", "is_announcement"]

    def generate_id(self, account, content, date):
        return hashlib.md5(f"{account}{content[:50]}{date}".encode()).hexdigest()

    def save_data(self, posts):
        # Save to latest_posts.csv (overwrite)
        with open(self.latest_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(posts)

        # Save to latest_posts.json
        with open(self.latest_json, 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=4, ensure_ascii=False)

        # Update archive (append unique)
        self.update_archive(posts)

    def update_archive(self, new_posts):
        existing_ids = set()
        if os.path.exists(self.archive_csv):
            with open(self.archive_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_ids.add(row['post_id'])

        file_exists = os.path.exists(self.archive_csv)
        with open(self.archive_csv, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            if not file_exists:
                writer.writeheader()
            for post in new_posts:
                if post['post_id'] not in existing_ids:
                    writer.writerow(post)

if __name__ == "__main__":
    # This part would be populated by the agent's research findings
    pass

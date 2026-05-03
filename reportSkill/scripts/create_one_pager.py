import os
from datetime import datetime
from data_loader import DataLoader
from topic_extractor import TopicExtractor

class ReportGenerator:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def generate(self):
        loader = DataLoader(self.input_file)
        posts = loader.load()
        
        if not posts:
            print("No data found to generate report.")
            return

        extractor = TopicExtractor()
        topics = extractor.extract(posts)
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        report = []
        report.append(f"# Executive Branch Monitoring Report - {date_str}")
        report.append("\n## Summary")
        report.append(f"Analyzed {len(posts)} recent publications from official accounts.")
        
        report.append("\n## Main Topics Identified")
        for topic, count in topics:
            report.append(f"- **{topic}**: {count} mentions")
            
        report.append("\n## Representative Posts")
        for post in posts[:3]: # Show top 3
            report.append(f"### {post['account']} ({post['platform']})")
            report.append(f"*{post['date']}*")
            report.append(f"\n{post['content']}")
            report.append(f"\n[View Post]({post['url']})")
            report.append("\n---")
            
        report.append("\n## Monitoring Details")
        report.append(f"- **Input File:** {self.input_file}")
        report.append("- **Format:** One-page Summary (Markdown)")
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(report))
        
        print(f"Report generated: {self.output_file}")

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    input_path = os.path.join(base_dir, "outputs", "latest_posts.csv")
    output_path = os.path.join(base_dir, "outputs", f"executive_branch_report_{datetime.now().strftime('%Y-%m-%d')}.md")
    
    generator = ReportGenerator(input_path, output_path)
    generator.generate()

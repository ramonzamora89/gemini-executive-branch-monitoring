import os
from datetime import datetime
from data_loader import DataLoader
from topic_extractor import TopicExtractor
from weasyprint import HTML

class HTMLReportGenerator:
    def __init__(self, input_file, template_file, output_html, output_pdf):
        self.input_file = input_file
        self.template_file = template_file
        self.output_html = output_html
        self.output_pdf = output_pdf

    def generate(self):
        loader = DataLoader(self.input_file)
        posts = loader.load()
        
        if not posts:
            print("No data found to generate report.")
            return

        extractor = TopicExtractor()
        topics = extractor.extract(posts)
        
        with open(self.template_file, 'r', encoding='utf-8') as f:
            template = f.read()

        # Data Preparation
        date_str = datetime.now().strftime("%Y-%m-%d")
        document_title = f"Executive branch monitoring summary — {date_str}"
        category = "Government monitoring"
        
        # Main topics as points
        highlights_html = ""
        for topic, count in topics:
            highlights_html += f"<li><strong>{topic}</strong> was mentioned {count} times in recent posts.</li>\n"

        # Stats section
        stats_html = ""
        stats_html += f'<div class="stat-item"><div class="stat-number">{len(posts)}</div><div class="stat-label">Total posts analyzed</div></div>\n'
        
        accounts = set(p['account'] for p in posts)
        stats_html += f'<div class="stat-item"><div class="stat-number">{len(accounts)}</div><div class="stat-label">Official accounts monitored</div></div>\n'

        # Main content
        latest_posts_html = ""
        for post in posts[:3]:
            latest_posts_html += f"<h3>{post['account']} ({post['platform']})</h3>"
            latest_posts_html += f"<p><em>{post['date']}</em><br>{post['content']}</p>"
            latest_posts_html += f'<p><a href="{post["url"]}">View original post</a></p><br>'

        # Replacement logic
        html = template
        
        # Applying Ramon Zamora Branding
        html = html.replace("--red: #CA3553;", "--red: #1a73e8;") # Update primary highlight color
        html = html.replace("Center for Cooperative Media", "Ramón Zamora")
        html = html.replace("Montclair State University", "Ruminations on tech, creativity and civics")
        html = html.replace("https://centerforcooperativemedia.org", "https://www.ramonzamora.co/")
        html = html.replace("info@centerforcooperativemedia.org", "ramonzamora89@gmail.com")
        html = html.replace("centerforcooperativemedia.org", "ramonzamora.co")
        
        # Updating content
        html = html.replace("[Document title in sentence case]", document_title)
        html = html.replace("[Category]", category)
        html = html.replace("[Opening paragraph that explains what this is about. Keep it concise and impactful.]", 
                            f"This report provides a concise summary of the latest public communications from the Guatemalan executive branch and President Bernardo Arévalo as of {date_str}.")
        html = html.replace("[Second paragraph with additional context or supporting information.]", 
                            "The monitoring focuses on transparency, judicial appointments, and economic policy announcements across X, Facebook, TikTok, and Instagram.")
        
        # Replace the list section
        html = html.replace("<li>[Key point 1 - keep each point to 1-2 lines]</li>", "")
        html = html.replace("<li>[Key point 2 - focus on impact and outcomes]</li>", "")
        html = html.replace("<li>[Key point 3 - use concrete numbers when possible]</li>", "")
        html = html.replace("<li>[Key point 4 - end with a forward-looking statement]</li>", highlights_html)
        
        # Replace the "How it works" section with "Latest Publications"
        html = html.replace("<h2>How it works</h2>", "<h2>Representative publications</h2>")
        html = html.replace("[Brief explanation of the process, approach, or methodology.]", latest_posts_html)

        # Replace stats
        html = html.replace('<div class="stat-item">\n                    <div class="stat-number">[Number]</div>\n                    <div class="stat-label">[What this number represents]</div>\n                </div>', stats_html, 1)
        html = html.replace('<div class="stat-item">\n                    <div class="stat-number">[Number]</div>\n                    <div class="stat-label">[What this number represents]</div>\n                </div>', "")

        # Contact and footer
        html = html.replace("[Contact name]", "Ramón Zamora")
        html = html.replace("[email@example.org]", "ramonzamora89@gmail.com")
        html = html.replace("[Phone number]", "")
        html = html.replace("[website-url.org]", "ramonzamora.co")
        html = html.replace("[action-url]", "https://ramonzamora.substack.com/")
        html = html.replace("Get Involved", "Subscribe on Substack")
        
        # Adding credit for the template
        credit_html = '<div style="font-size: 7pt; opacity: 0.6; margin-top: 10px; color: var(--white);">Template based on Center for Cooperative Media resources.</div>'
        html = html.replace('</div>\n            <a href="https://ramonzamora.substack.com/" class="cta">', f'{credit_html}</div>\n            <a href="https://ramonzamora.substack.com/" class="cta">')

        # Save HTML
        with open(self.output_html, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Professional HTML Report generated: {self.output_html}")
        
        # Generate PDF using WeasyPrint
        HTML(string=html).write_pdf(self.output_pdf)
        print(f"Professional PDF Report generated via WeasyPrint: {self.output_pdf}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
    input_path = os.path.join(base_dir, "outputs", "latest_posts.csv")
    template_path = os.path.join(base_dir, "plugins", "journalism-skills", "pdf-playground", "templates", "onepager-template.html")
    output_html = os.path.join(base_dir, "outputs", "executive_branch_one_pager.html")
    output_pdf = os.path.join(base_dir, "outputs", "executive_branch_one_pager.pdf")
    
    generator = HTMLReportGenerator(input_path, template_path, output_html, output_pdf)
    generator.generate()

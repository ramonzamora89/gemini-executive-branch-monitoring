import os
from datetime import datetime
from fpdf import FPDF
from data_loader import DataLoader
from topic_extractor import TopicExtractor

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Executive Branch Monitoring Report', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'R')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

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
        
        pdf = PDFReport()
        pdf.add_page()
        
        # Summary Section
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '1. Summary', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, f'This one-page report summarizes {len(posts)} recent publications from the Guatemalan executive branch and President Bernardo Arévalo.')
        pdf.ln(5)

        # Topics Section
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '2. Main Topics Identified', 0, 1)
        pdf.set_font('Arial', '', 12)
        for topic, count in topics:
            pdf.cell(0, 10, f'- {topic}: {count} mentions', 0, 1)
        pdf.ln(5)

        # Representative Posts
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, '3. Representative Posts', 0, 1)
        for post in posts[:3]:
            pdf.set_font('Arial', 'B', 11)
            pdf.cell(0, 8, f"{post['account']} ({post['platform']}) - {post['date']}", 0, 1)
            pdf.set_font('Arial', '', 10)
            # Ensure text is compatible with latin-1 for basic fpdf setup or handle encoding
            content = post['content'].encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 6, content)
            pdf.set_text_color(0, 0, 255)
            pdf.cell(0, 6, post['url'], 0, 1, link=post['url'])
            pdf.set_text_color(0, 0, 0)
            pdf.ln(4)

        # Monitoring Details
        pdf.set_y(-40)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 6, 'Monitoring Details:', 0, 1)
        pdf.set_font('Arial', '', 9)
        pdf.cell(0, 5, f'Input Source: {os.path.basename(self.input_file)}', 0, 1)
        pdf.cell(0, 5, 'Format: One-page PDF Summary', 0, 1)

        pdf.output(self.output_file)
        print(f"PDF Report generated: {self.output_file}")

if __name__ == "__main__":
    # Correct pathing relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
    input_path = os.path.join(base_dir, "outputs", "latest_posts.csv")
    output_path = os.path.join(base_dir, "outputs", "executive_branch_one_pager.pdf")
    
    generator = ReportGenerator(input_path, output_path)
    generator.generate()

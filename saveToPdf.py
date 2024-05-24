from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

class savetoPDF:

    def create_pdf_from_text(self, text, output_filename):
        # Create a PDF document
        doc = SimpleDocTemplate(output_filename, pagesize=letter)
        
        # Create a stylesheet for formatting
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_body = styles['BodyText']
        
        # Parse the text and add paragraphs and headings to the PDF
        content = []
        for line in text.split('\n'):
            if line.startswith('#'):
                content.append(Paragraph(line.strip('#').strip(), style_heading))
            else:
                content.append(Paragraph(line, style_body))
        
        # Add the content to the PDF document
        return doc.build(content)


from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf_report(response_content, table_data=None):
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=60, leftMargin=60, topMargin=60, bottomMargin=60)
    styles = getSampleStyleSheet()
    styles['Normal'].fontSize = 12
    content = []

    try:
        # Add text content to the PDF
        lines = response_content.split('\n')
        for line in lines:
            paragraph = Paragraph(line, styles['Normal'])
            content.append(paragraph)
            content.append(Spacer(1, 12))

        if table_data:
            data = [list(row) for row in table_data]
            table = Table(data)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]))
            content.append(Paragraph('Table:', styles['Normal']))
            content.append(Spacer(1, 12))
            content.append(table)
            content.append(Spacer(1, 12))

        # Build the PDF and return buffer
        pdf.build(content)
        buffer.seek(0)
        return buffer.getvalue()

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


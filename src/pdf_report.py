from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def create_pdf_with_letterhead(timestamp, ):
    """
    Create a PDF report with a letterhead and a table of data.
    Args:
        timestamp (str): The timestamp to include in the PDF filename.
    """
    # Create the PDF
    pdf = SimpleDocTemplate("report_with_letterhead.pdf", pagesize=LETTER)

    # Set up styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    subheader_style = styles["Heading2"]
    body_style = styles["BodyText"]

    # Elements to add to the PDF
    elements = []

    # Add letterhead image (adjust size/position as needed)
    letterhead = Image("CLI_Logo.png", width=2.0*inch, height=1.0*inch)
    title1 = Paragraph("Pleasure Craft Courtesy Check", subheader_style)
    # Put them side-by-side in a table
    table_header = Table([[letterhead, title1]], colWidths=[150, 300])  # adjust widths as needed
    elements.append(table_header)

    # Add intro text
    
    intro = """
    This report summarizes the results of a Pleasure Craft Courtesy Check performed by the Canadian Lifeboat Institution.
    """
    elements.append(Paragraph(intro, body_style))

    # Add title
    #elements.append(Paragraph("Canadian Lifeboat Institution", title_style))
    elements.append(Spacer(1, 0.1 * inch))
    elements.append(Paragraph("Report Date: " + timestamp.strftime("%B %d, %Y"), body_style))
    elements.append(Spacer(1, 0.1 * inch))
    
    # Add table data (6 rows)
    elements.append(Paragraph("Vessel Information", body_style))
    data = [
        ["", "", ""],
        ["Name", "Test", "10"],
        ["Type", "Sail", "5"],
        ["Length", "34", "7"],
        ["", "Sweet Green Pears", "6"],
        ["", "Seasonal Peaches", "4"],
        ["", "Seedless Grapes", "8"],
    ]

    # Create the table with styling
    table = Table(data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * inch))

    # Add body text
    text = """
    This report summarizes the inventory activity for the current month. The numbers above reflect fresh produce received and distributed to various branches. Please ensure all records are verified and reported by the end of the week.
    """
    elements.append(Paragraph(text, body_style))

    # Build the PDF
    pdf.build(elements)

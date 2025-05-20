from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Create the PDF
pdf = SimpleDocTemplate("report_with_letterhead.pdf", pagesize=LETTER)

# Set up styles
styles = getSampleStyleSheet()
title_style = styles["Title"]
body_style = styles["BodyText"]

# Elements to add to the PDF
elements = []

# Add letterhead image (adjust size/position as needed)
letterhead = Image("letterhead.png", width=6.5*inch, height=1.0*inch)
elements.append(letterhead)
elements.append(Spacer(1, 0.25 * inch))

# Add title
elements.append(Paragraph("Monthly Activity Report", title_style))
elements.append(Spacer(1, 0.25 * inch))

# Add table data (6 rows)
data = [
    ["Item", "Description", "Quantity"],
    ["Apples", "Fresh Red Apples", "10"],
    ["Oranges", "Juicy Oranges", "5"],
    ["Bananas", "Ripe Bananas", "7"],
    ["Pears", "Sweet Green Pears", "6"],
    ["Peaches", "Seasonal Peaches", "4"],
    ["Grapes", "Seedless Grapes", "8"],
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
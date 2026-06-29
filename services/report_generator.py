from reportlab.pdfgen import canvas

def create_report(score, filename):

    pdf = canvas.Canvas(filename)

    pdf.drawString(100, 750, "Resume Analysis Report")

    pdf.drawString(100, 720, f"ATS Score : {score}")

    pdf.save()
import glob
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

filepaths = glob.glob("*.txt")
for filepath in filepaths:
    page_title = filepath.split(".")[0].capitalize()

    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=10, txt=page_title, ln=1)

    with open(filepath, 'r') as file:
        text = file.readlines()
        pdf.set_font(family="Times", size=14)

        pdf.multi_cell(w=0, h=10, txt="".join(text))

pdf.output("animals.pdf")

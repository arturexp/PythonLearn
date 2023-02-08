# Generating pdf file from csv file

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    #  w - cell до конца страницы
    #  ln - новая строка
    #  size - высота cell
    #  align - текст слева
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    #  координаты начала и конца лини ив unit
    #  x1, y1, x2, y2
    pdf.line(10, 21, 200, 21)

    pdf.ln(265)
    #  set the footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(277)
        #  set the footer
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")

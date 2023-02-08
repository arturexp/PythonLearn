import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# get files in list
filepaths = glob.glob("*.xlsx")

for filepath in filepaths:
   #  new FPDF instance
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    #  geting title for page
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    #  import data from file into pandas
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #  table header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in df.columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    #  print table with content
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    #  creating pdf files
    pdf.output(f"PDFs/{filename}.pdf")

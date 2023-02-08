import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# get files in list
filepaths = glob.glob("*.xlsx")

for filepath in filepaths:
    #  import data from file into pandas
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    #  new FPDF instance
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    #  geting title for page
    filename = Path(filepath).stem
    invoice_nr = filename.split(".")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}")
    #  creating pdf files
    pdf.output(f"PDFs/{filename}.pdf")

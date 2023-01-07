import fpdf
import pandas
import pandas as pd
db = pandas.read_csv("topics.csv", sep=',')
pdf = fpdf.FPDF(orientation='P', unit = 'mm', format = 'A4')

for index, data in db.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=data["Topic"], align='L', ln=1)
    pdf.line(10, 21, 200, 22)
    for i in range(int(data["Pages"]) - 1):
        pdf.add_page()

pdf.output("Output.pdf")
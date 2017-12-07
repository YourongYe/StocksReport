#https://stackoverflow.com/questions/14928057/reportlab-text-background-size-doesnt-match-font-size

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import PageTemplate, Frame, NextPageTemplate, BaseDocTemplate, SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import cm

OUT_PATH = "./out/"
DELIM = "|"

class ReportGenerator:
    report = []
    tickers = []

    def load_ticker(self,ticker_file_path):
        if not os.path.isfile(ticker_file_path):
            print("File not exist ["+filename+"]")
            return False

        ticker_file = open(ticker_file_path,"r")
        for line in ticker_file:
            self.tickers.append(line.strip())

        ticker_file.close();
        return True

    def create_chart(self,file_path):
        if not os.path.isfile(file_path):
            print("File not exist ["+file_path+"]")
            return False

        im = Image(file_path,width=10*cm,height=3.8*cm)
        self.report.append(im)
        return True

    def generateReport(self, file_path):
        print("Generating report")
        doc = SimpleDocTemplate(file_path,pagesize=letter,
                    rightMargin=30,leftMargin=30,
                    topMargin=30,bottomMargin=30)

        for ticker in self.tickers:
            print("Handling ["+ticker+"]")
            chart_file = OUT_PATH+ticker+"_chart.png"
            if not os.path.isfile(chart_file):
                print("File not exist ["+file_path+"]")
                continue
            self.report.append(Paragraph("Ticker: "+ticker,getSampleStyleSheet()["Normal"]))
            self.create_chart(chart_file)

        # Build Document
        doc.build(self.report)

if __name__ == "__main__":
    generator = ReportGenerator()
    generator.load_ticker(OUT_PATH+"tickers.txt")
    generator.generateReport(OUT_PATH+"report.pdf")

#!/bin/sh

/home/user/mizhang/miniconda3/bin/python py_screenshot_batch.py

/home/user/mizhang/miniconda3/bin/python pdf_report_generator.py

echo "Sending email"
echo "Tickers report" | mailx -s "Tickers report" -a "./out/report.pdf" mizhang@factset.com

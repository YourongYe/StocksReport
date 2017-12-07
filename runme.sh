#!/bin/sh

python py_screenshot_batch.py

python pdf_report_generator.py

echo "Sending email"
echo "Tickers report" | mailx -s "Tickers report" -a "./out/report.pdf" yourong.ye@hotmail.com

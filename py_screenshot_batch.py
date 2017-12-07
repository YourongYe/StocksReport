from PIL import Image
import os
out_path = "./out/"
ticker_file = open(out_path+"tickers.txt","r")
tickers = []
for line in ticker_file:
    tickers.append(line.strip())
ticker_file.close();

for ticker in tickers:
    # Screenshot
    system_cmd = "phantomjs js_screenshot.js " + ticker
    print("running system cmd: ["+system_cmd+"]")
    os.system(system_cmd)

    # Cropping
    print("Cropping")
    img_name = out_path+ticker+".png"
    if os.path.isfile(img_name):
        print("handling ["+img_name+"]")
        img = Image.open(img_name)
        #left, upper, right, lower
        area = (20, 435, 650, 675)
        img.crop(area).save(out_path+ticker+"_chart.png")


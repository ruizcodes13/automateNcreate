#pip install tk
#pip install ghostscript            These must be installed first before install camelot
#pip install camelot-py
#Now procedure with code below

import camelot as cl

tables = camelot.read_pdf('file.pdf', pages='1') #file.pdf is what pdf you are using and selecting what page
print(tables)

#now import table to CSV format
tables.export('file.csv', f='csv', compress=True)
tables[0].to_csv(file.csv)  

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current directory.
for csvFile in os.listdir('.'):
    if not csvFile.endswith('.csv'):
        continue
    print('Removing header from ' + csvFile + '...')

    # Read the CSV file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFile)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # Write the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFile), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

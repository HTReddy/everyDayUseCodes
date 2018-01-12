import pandas
import pprint
import json

jsonDataFrame = {}

def convertExcelToJson(excelFileName=None, jsonFileName=None):
    dataFrame = pandas.read_excel(excelFileName)
    pprint.pprint(dataFrame.columns)  # All the headings of your excel file, these can become the source for JSON Keys
    # Iterate through all the excel sheet headings and store in a dictionary
    for everyHeading in dataFrame.columns:
        jsonDataFrame[str(everyHeading)] = dataFrame[str(everyHeading)].values.tolist() # Helps extract the contents under a heading
    # Dump the dictionary to a JSON
    with open(jsonFileName, 'w') as fp:
        json.dump(jsonDataFrame, fp)

convertExcelToJson(excelFileName="yourInputExcel.xlsx", jsonFileName="outputJson.json")
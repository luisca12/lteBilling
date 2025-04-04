from log import authLog
from functions import checkIsDigit
from strings import inputErrorString, menuString, greetingString

import pandas as pd
import openpyxl
import traceback
import sys
import re
import os

outFile = "Filtered file with Phone Number, IP and site code.xlsx"

openGearPatt = re.compile(r'opengear', re.IGNORECASE)
newNumberList = []
newStaticIP = []
newSiteCode = []

def lteBilling():

    try:
        # Load the Excel file
        file = 'Enterprise M2M account.xlsx'  # <- Replace this with your actual file path
        authLog.info(f"File found successfully: {file}")
        generalListSheet = pd.read_excel(file, sheet_name=0)
        authLog.info(f"generalListSheet loaded successfully: {generalListSheet}")
        verizonSheet = pd.read_excel(file, sheet_name=1)
        authLog.info(f"verizonSheet loaded successfully: {verizonSheet}")

        # Ensure the correct columns: B in generalListSheet (index 1), D and G in verizonSheet (indices 3 and 6)
        generalListSheet_values = generalListSheet.iloc[:, 1].astype(str)  # Column B from Sheet 1
        phoneNumberList = list(verizonSheet.iloc[:, 3])  # Columns D and G from Sheet 2
        staticIPList = list(verizonSheet.iloc[:, 4])
        siteCodeList = list(verizonSheet.iloc[:, 6])
        vendorList = list(verizonSheet.iloc[:, 7])

        authLog.info(f"Values from General Sheet and Verizon Sheet saved:\nGeneralList:\n{generalListSheet_values}\n" \
                     f"Phone Number List:\n{phoneNumberList}\nStatic IP List:\n{staticIPList}\nSite Code List:\n{siteCodeList}\n" \
                     f"Vendor List:\n{vendorList}"
                     )

        # for item in vendorList:
        #    print(vendorList)

        for vendor, phoneNumber, staticIP, siteCode in zip(vendorList, phoneNumberList, staticIPList, siteCodeList, ):
            if openGearPatt.search(str(vendor)): 
                newNumberList.append(phoneNumber)
                authLog.info(f"Phone Number: {phoneNumber} appended to newNumberList")
                newStaticIP.append(staticIP)
                authLog.info(f"Static IP: {staticIP} appended to newStaticIP")
                newSiteCode.append(siteCode)
                authLog.info(f"Site Code: {siteCode} appended to newSiteCode")
        
        print(f"INFO: Vendor List amount: {len(vendorList)}")
        print(f"INFO: newNumberList amount {len(newNumberList)}")
        authLog.info(f"Vendor List amount: {len(vendorList)}\nnewNumberList amount {len(newNumberList)}")

        dataFrame = pd.DataFrame({
            'Phone Number' : newNumberList,
            'Static IP': newStaticIP,
            'Site Code' : newSiteCode
        })
        authLog.info(f"Data Frame created for file: {file}, Data Frame: {dataFrame}")

        authLog.info(f"Creating the new file only with cell values that matched OpenGear from file: {file}")
        dataFrame.to_excel(outFile, index=False)

        filteredSheet = pd.read_excel(outFile, sheet_name=0)

        filteredSheetValues = filteredSheet.iloc[:, [0, 1]].astype(str)

        # for item, item1 in zip(filteredSheetValues.iloc[:, 0], filteredSheetValues.iloc[:, 1]):
        #     print(f"{item}:{item1}")

        #  Create a lookup dictionary from verizonSheet
        lookup_dict = dict(zip(filteredSheetValues.iloc[:, 0], filteredSheetValues.iloc[:, 1]))

        # print(lookup_dict)

        print(generalListSheet_values)

        for key,val in lookup_dict.items():
            if '3174719505' in key:
                print(f"Math found: 3174719505 : {key}")

        # Map the values from generalListSheet Column B using the lookup
        generalListSheet['Matched Value From Filtered File and Enterprise M2M Account'] = generalListSheet_values.map(lookup_dict)

        # Optionally, save the updated generalListSheet to a new Excel file
        generalListSheet.to_excel('OpenGear IPs.xlsx', index=False)

    except FileNotFoundError:
        print(f"Couldn't find file {file}. Please check the file name and try again, remember to include the .xlsx")
        authLog.error(f"File not found in path {file}\n{traceback.format_exc()}")
        os.system("PAUSE")

    except Exception as error:
        print(f"Got an error when trying to load the workbook from file: {file}, error: {error}")
        authLog.error(f"Wasn't possible to choose the XLSX file: {file}, error message: {error}\n{traceback.format_exc()}")
        os.system("PAUSE")
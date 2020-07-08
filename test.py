import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("test").get_worksheet(1)

data = sheet.get_all_records()
#col1 = sheet.col_values
#row = sheet.row_values(3)
#col = sheet.col_values(2)
#col1 = sheet.col_values(1)
#cell = sheet.cell(2,11).value

#insertRow = ["hello", 5, "red", "blue"]
#sheet.update_cell(2,2, "CHANGED")
#numRows = sheet.row_count
pprint(data)
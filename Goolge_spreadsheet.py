import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("Cricket Alerts-a5d7fc29cc02.json",scope)
client = gspread.authorize(creds)
sheet = client.open("scoreboards").sheet1
data = sheet.get_all_records()
pprint(data)

val = sheet.row_values(1)
val1 = sheet.row_values(2)
pprint(val)
pprint(val1)

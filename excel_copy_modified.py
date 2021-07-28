import win32com.client as win32
from pathlib import Path
#from selenium import webdriver
import os
import webbrowser
import time

# Use com to copy the files around
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = True
excel.DisplayAlerts = False

# Define the full path for the data file file
data_file = Path.cwd() / "Input.xlsx"

def exc_cop(a,b,c):
	# Open up the data file
	wb_data = excel.Workbooks.Open(data_file)

	# Copy from the data file (select all data in A:D columns)
	wb_data.Worksheets("Sheet1").Range(a).Select()

	webbrowser.open('https://www.python.org')
	time.sleep(5)
	
	os.system("taskkill /im chrome.exe /f")
	time.sleep(5)
	
	# Paste into the template file
	try:
		excel.Selection.Copy(Destination=wb_data.Worksheets("Sheet1").Range(b))
	except:
		print('Copy-paste operation failed to complete.')
	ws = wb_data.Worksheets('Sheet2')
	ws.Cells(c,2).Value = 'Pass'
	
	# Must convert the path file object to a string for the save to work
	wb_data.SaveAs(str(data_file))
	return print("Test run completed!!")


exc_cop("A:A","B1",2)

exc_cop("E1:F3","H1:I3",3)

excel.Application.Quit()
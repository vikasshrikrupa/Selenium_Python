import unittest
import openpyxl
from openpyxl.styles import PatternFill
wb = openpyxl.load_workbook(r'F:\Python\Python_New\Praticals\Class\Input.xlsx')
sheet = wb['Sheet1']

class TestExcel(unittest.TestCase):
	def test_copy(self):
		a = sheet['A1']
		b = sheet['E1']
		msg1 = "Orginal cell value and copied cell value are not equal!!"
		self.assertEqual( a.value, b.value, msg1)
	def test_color(self):
		a = sheet['A1']
		b = sheet['E1']
		msg2 = "Orginal cell fill color and copied cell  fill color are not equal !"
		self.assertEqual( a.fill.fgColor.rgb, b.fill.fgColor.rgb, msg2)
	def test_font(self):
		a = sheet['A1']
		b = sheet['E1']
		msg3 = "Orginal cell font size and copied cell font size are not equal !"
		self.assertEqual( a.font.size, b.font.size, msg3)
		
print("Tests run completed!!")

if __name__ == '__main__':
	log_file = 'log_file.txt'
	with open(log_file, "w") as f:
		runner = unittest.TextTestRunner(f)
		unittest.main(testRunner=runner)
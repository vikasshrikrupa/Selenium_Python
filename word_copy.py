import win32com.client as win32
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False 
doc = word.Documents.Open(r'F:\Python\Python_New\Praticals\Class\Table.docx')

doc.Select() #select everything
word.Selection.Copy()
word.Selection.GoTo(win32.constants.wdGoToPage, win32.constants.wdGoToAbsolute)
word.Selection.Paste()

doc.Close(SaveChanges=True)
word.Quit()
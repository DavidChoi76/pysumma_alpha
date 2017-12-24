#Unit Test 1 : Open Decision file - Edit analysis period - Save Decision file

from Decisions import Decisions

path = 'D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\pysumma\\'
filename = 'Decision.txt'

Decisionfile = Decisions(path, filename)
selectlines = Decisionfile.OpenRead()

print("Date input format : (ex) YYYY-MM-DD HH:MM")
StartDate = input("(01) simulation start time : ")
Decisions.SetStartDateFunction(StartDate, selectlines)

print("Date input format : (ex) YYYY-MM-DD HH:MM")
EndDate = input("(02) simulation end time : ")
Decisions.SetEndDateFunction(EndDate, selectlines)

Decisionfile.EditSave(selectlines)
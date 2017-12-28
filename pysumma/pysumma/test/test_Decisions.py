from pysumma.pysumma.Decisions import Decisions

path = 'D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\'
filename = 'Decision.txt'

Decisionfile = Decisions(path, filename)
selectlines = Decisionfile.OpenRead()

def test_OpenRead():
    path = 'D:\\pysumma\\pysumma_alpha0\\pysumma\\pysumma\\'
    filename = 'Decision.txt'
    Decisionfile = Decisions(path, filename)
    selectlines = Decisionfile.OpenRead()
    assert(len(selectlines[1]) > 1)

def test_SetSoilCategoryDatasetFunction():
    test_method = Decisions.SetSoilCategoryDatasetFunction('STAS', selectlines)
    assert(len(test_method) > 1)

def test_SetSoilMoistureControlFunction():
    test_method = Decisions.SetSoilMoistureControlFunction('NoahType', selectlines)
    assert (len(test_method) > 1)

def test_EditSave():
    test_save = Decisionfile.EditSave(selectlines)
    assert (len(test_save) > 1)

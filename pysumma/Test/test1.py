from pysumma.pysumma.Decisions import Decisions

path = 'D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\pysumma\\'
filename = 'Decision.txt'

Decisionfile = Decisions(path, filename)
selectlines = Decisionfile.OpenRead()

name3 = input("(03) Select STAS or STAS-RUC or ROSETTA : ")
Decisions.SetSoilCategoryDatasetFunction(name3, selectlines)

name4 = input("(04) Select USGS or MODIFIED_IGBP_MODIS_NOAH : ")
Decisions.SetVegetationCategoryDatasetFunction(name4, selectlines)

name5 = input("(05) Select NoahType or CLM_Type or SiB_Type : ")
Decisions.SetSoilMoistureControlFunction(name5, selectlines)

name6 = input("(06) Select BallBerry or Jarvis : ")
Decisions.SetStomatalResistanceFunction(name6, selectlines)

name7 = input("(07) Select itertive or non_iter or itersurf : ")
Decisions.SetNumericalMethodFunction(name7, selectlines)

name8 = input("(08) Select numericl or analytic : ")
Decisions.SetFluxDerivativesFunction(name8, selectlines)

name9 = input("(09) Select monTable or specified : ")
Decisions.SetLAIandSAIFunction(name9, selectlines)

name10 = input("(10) Select moisture or mixdform : ")
Decisions.SetRichardsEquationFunction(name10, selectlines)

Decisionfile.EditSave(selectlines)
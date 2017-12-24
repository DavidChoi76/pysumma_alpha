from pysumma.pysumma.Decisions import Decisions

path = 'D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\pysumma\\'
filename = 'Decision.txt'

Decisionfile = Decisions(path, filename)
selectlines = Decisionfile.OpenRead()

name11 = input("(11) Select qTopmodl or bigBuckt or noXplict : ")
Decisions.SetGroundwaterRarameterizationFunction(name11, selectlines)

name12 = input("(12) Select constant or pow_prof : ")
Decisions.SetHydraulicConductivityProfileFunction(name12, name11, selectlines)

name13 = input("(13) Select presTemp or nrg_flux : ")
Decisions.SetUpperBoundaryConditionsForThermodynamicsFunction(name13, selectlines)

name14 = input("(14) Select presTemp or zeroFlux : ")
Decisions.SetLowerBoundaryConditionsForThermodynamicsFunction(name14, selectlines)

name15 = input("(15) Select presHead or liq_flux : ")
Decisions.SetUpperBoundaryConditionsForSoilHydrologyFunction(name15, name13, name14,  selectlines)

name16 = input("(16) Select drainage or presHead or bottmPsi or zeroFlux : ")
Decisions.SetLowerBoundaryConditionsForSoilHydrologyFunction(name16, name13, name14,  selectlines)

name17 = input("(17) Select Raupach_BLM1994 or CM_QJRMS1998 or vegTypeTable : ")
Decisions.SetParameterizationForVegetationFunction(name17, selectlines)

name18 = input("(18) Select simplExp or difTrans : ")
Decisions.SetParameterizationForCanopyEmissivityFunction(name18, selectlines)

name19 = input("(19) Select stickySnow or lightSnow : ")
Decisions.SetParameterizationForSnowInterceptionFunction(name19, selectlines)

name20 = input("(20) Select exponential or logBelowCanopy : ")
Decisions.SetWindProfileFunction(name20, selectlines)

Decisionfile.EditSave(selectlines)
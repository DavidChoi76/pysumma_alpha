from pysumma.pysumma.Decisions import Decisions

path = 'D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\pysumma\\'
filename = 'Decision.txt'

Decisionfile = Decisions(path, filename)
selectlines = Decisionfile.OpenRead()

name11 = input("(11) Select qTopmodl or bigBuckt or noXplict : ")
Decisions.SetGroundwaterRarameterizationFunction(name11, selectlines)

name21 = input("(21) Select standard or louisinv or mahrtexp : ")
Decisions.SetStabilityFunction(name21, selectlines)

name22 = input("(22) Select noah_mp or CLM_2stream or UEB_2stream or NL_scatter or BeersLaw : ")
Decisions.SetCanopyShortwaveRadiationMethodFunction(name22, selectlines)

name23 = input("(23) Select conDecay or varDecay : ")
Decisions.SetAlbedoRepresentationFunction(name23, selectlines)

name24 = input("(24) Select consettl or anderson : ")
Decisions.SetCompactionRoutineFunction(name24, selectlines)

name25 = input("(25) Select CLM_2010 or jrdn1991 : ")
Decisions.SetSnowLayersFunction(name25, selectlines)

name26 = input("(26) Select tyen1965 or melr1977 or jrdn1991 or smnv2000 : ")
Decisions.SetThermalConductivityRepresentationForSnowFunction(name26, selectlines)

name27 = input("(27) Select funcSoilWet or mixConstit or hanssonVZJ : ")
Decisions.SetThermalConductivityRepresentationForSoilFunction(name27, selectlines)

name28 = input("(28) Select localColumn or singleBasin : ")
Decisions.SetSpatialRepresentationOfGroundwaterFunction(name28, name11, selectlines)

name29 = input("(29) Select timeDlay or qInstant : ")
Decisions.SetSubGridRoutingFunction(name29, selectlines)

Decisionfile.EditSave(selectlines)
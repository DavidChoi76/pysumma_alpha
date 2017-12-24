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
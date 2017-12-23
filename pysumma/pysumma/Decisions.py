#import os

class Decisions:

	def __init__(self, path, filename):
		self.path = path
		self.filename = filename

	def OpenRead(self):
		filepath = self.path+self.filename
		fileopen = open(filepath, 'rt')
		lines = fileopen.readlines()
		return lines

	def SetStartDateFunction(name):
		selectlines[9] = "simulStart              '%s'                   ! (01) simulation start time -- must be in single quotes \n" % name
		return selectlines[9]

	def SetEndDateFunction(name):
		selectlines[10] = "simulFinsh             '%s'                   ! (02) simulation end time -- must be in single quotes \n" % name

	def SetSoilCategoryDatasetFunction(name):
		if name == "STAS" or name == "STAS-RUC" or name == "ROSETTA":
			pass
		else:
			print("Check your input at (03) SetStomatalResistanceFunction !! ")
		selectlines[12] = 'soilCatTbl                      %s            ! (03) soil-category dateset \n' % name
		return selectlines[12]

	def SetVegetationCategoryDatasetFunction(name):
		if name == "USGS" or name == "MODIFIED_IGBP_MODIS_NOAH":
			pass
		else:
			print("Check your input at (04) SetStomatalResistanceFunction !! ")
		selectlines[13] = 'vegeParTbl                      %s            ! (04) vegetation category dataset \n' % name
		return selectlines[13]

	def SetSoilMoistureControlFunction(name):
		if name == "NoahType" or name == "CLM_Type" or name == "SiB_Type":
			pass
		else:
			print("Check your input at (05) SetSoilCategoryDatasetFunction !! ")
		selectlines[14] = 'soilStress                      %s            ! (05) choice of function for the soil moisture control on stomatal resistance \n' % name
		return selectlines[14]

	def SetStomatalResistanceFunction(name):
		if name == "BallBerry" or name == "Jarvis":
			pass
		else:
			print("Check your input at (06) SetStomatalResistanceFunction !! ")
		selectlines[15] = 'stomResist                      %s            ! (06) choice of function for stomatal resistance \n' % name
		return selectlines[15]

	def SetNumericalMethodFunction(name):
		if name == "itertive" or name == "non_iter" or name == "itersurf":
			pass
		else:
			print("Check your input at (07) SetNumericalMethodFunction !! ")
		selectlines[17] = 'num_method                      %s            ! (07) choice of numerical method \n' % name
		return selectlines[17]

	def SetFluxDerivativesFunction(name):
		if name == "numericl" or name == "analytic":
			pass
		else:
			print("Check your input at (08) SetFluxDerivativesFunction !! ")
		selectlines[18] = 'fDerivMeth                      %s            ! (08) method used to calculate flux derivatives \n' % name
		return selectlines[18]

	def SetLAIandSAIFunction(name):
		if name == "monTable" or name == "specified":
			pass
		else:
			print("Check your input at (09) SetLAIandSAIFunction !! ")
		if (name == 'specified'):
			print("LAI and SAI method option ['specified'] is no longer supported !! ")
		selectlines[19] = 'LAI_method                      %s            ! (09) method used to determine LAI and SAI \n' % name
		return selectlines[19]

	def SetRichardsEquationFunction(name):
		if name == "moisture" or name == "mixdform":
			pass
		else:
			print("Check your input at (10) SetRichardsEquationFunction !! ")
		selectlines[20] = 'f_Richards                      %s            ! (10) form of Richards equation \n' % name
		return selectlines[20]

	def SetGroundwaterRarameterizationFunction(name):
		if name == "qTopmodl" or name == "bigBuckt" or name == "noXplict":
			pass
		else:
			print("Check your input at (11) SetGroundwaterRarameterizationFunction !! ")
		if (name == 'qTopmodl'):
			print("you selected 'qTopmodl'. Therefore you have to select 'zeroFlux' at (16) SetLowerBoundaryConditionsForSoilHydrologyFunction !! ")
		selectlines[21] = 'groundwatr                      %s            ! (11) choice of groundwater parameterization \n' % name
		return selectlines[21]

	def SetHydraulicConductivityProfileFunction(name):
		if name == "constant" or name == "pow_prof":
			pass
		else:
			print("Check your input at (12) SetHydraulicConductivityProfileFunction !! ")
		if name == 'pow_prof':
			if name11 == "qTopmodl":
				pass
			else:
				print("You selected '%s' at (11) SetGroundwaterRarameterizationFunction.\n"
					  "'pow_prof' must be selected at (12) SetHydraulicConductivityProfileFunction when using 'qTopmodl' at (11) SetGroundwaterRarameterizationFunction" %name11)
		selectlines[22] = 'hc_profile                      %s            ! (12) choice of hydraulic conductivity profile \n' % name
		return selectlines[22]

	def SetUpperBoundaryConditionsForThermodynamicsFunction(name):
		if name == "presTemp" or name == "nrg_flux":
			pass
		else:
			print("Check your input at (13) SetUpperBoundaryConditionsForThermodynamicsFunction !! ")
		if (name == 'presTemp'):
			print("you selected 'presTemp'. Therefore you have to select 'presHead' at (15) SetUpperBoundaryConditionsForSoilHydrologyFunction and (16) SetLowerBoundaryConditionsForSoilHydrologyFunction !! ")

		selectlines[23] = 'bcUpprTdyn                      %s            ! (13) type of upper boundary condition for thermodynamics \n' % name
		return selectlines[23]

	def SetLowerBoundaryConditionsForThermodynamicsFunction(name):
		if name == "presTemp" or name == "zeroFlux":
			pass
		else:
			print("Check your input at (14) SetLowerBoundaryConditionsForThermodynamicsFunction !! ")
		selectlines[24] = 'bcLowrTdyn                      %s            ! (14) type of lower boundary condition for thermodynamics \n' % name
		return selectlines[24]

	def SetUpperBoundaryConditionsForSoilHydrologyFunction(name):
		if name == "presHead" or name == "liq_flux":
			pass
		else:
			print("Check your input at (15) SetUpperBoundaryConditionsForSoilHydrologyFunction !! ")
		if name == 'presHead':
			if name13 == "presTemp" and name14 == "zeroFlux":
				pass
			else:
				print("You selected '%s' at (13) SetUpperBoundaryConditionsForThermodynamicsFunction and '%s' at (14) SetLowerBoundaryConditionsForThermodynamicsFunction.\n"
					  "'presHead' must be selected at (15) SetUpperBoundaryConditionsForSoilHydrologyFunction when using 'presTemp' at (13) SetUpperBoundaryConditionsForThermodynamicsFunction.\n"
					  "'presHead' must be selected at (15) SetUpperBoundaryConditionsForSoilHydrologyFunction when using 'zeroFlux' at (14) SetUpperBoundaryConditionsForThermodynamicsFunction.", name13, name14)
		selectlines[25] = 'bcUpprSoiH                      %s            ! (15) type of upper boundary condition for soil hydrology \n' % name
		return selectlines[25]

	def SetLowerBoundaryConditionsForSoilHydrologyFunction(name):
		if name == "drainage" or name == "presHead" or name == "bottmPsi" or name == "zeroFlux" :
			pass
		else:
			print("Check your input at (16) SetLowerBoundaryConditionsForSoilHydrologyFunction !! ")
		if name == 'presHead':
			if name13 == "presTemp" and name14 == "zeroFlux":
				pass
			else:
				print("You selected '%s' at (13) SetUpperBoundaryConditionsForThermodynamicsFunction and '%s' at (14) SetLowerBoundaryConditionsForThermodynamicsFunction.\n"
					  "'presHead' must be selected at (16) SetUpperBoundaryConditionsForSoilHydrologyFunction when using 'presTemp' at (13) SetUpperBoundaryConditionsForThermodynamicsFunction.\n"
					  "'presHead' must be selected at (16) SetUpperBoundaryConditionsForSoilHydrologyFunction when using 'zeroFlux' at (14) SetUpperBoundaryConditionsForThermodynamicsFunction.", name13, name14)
		if name11 == 'qTopmodl':
			if name == "zeroFlux":
				pass
			else:
				print("You selected '%s' at (11) SetGroundwaterRarameterizationFunction.\n"
					  "When you select 'qTopmodl' at (11) SetGroundwaterRarameterizationFunction, you have to select 'zeroFlux' at (16) SetLowerBoundaryConditionsForSoilHydrologyFunction" %name11)
		selectlines[26] = 'bcLowrSoiH                      %s            ! (16) type of lower boundary condition for soil hydrology \n' % name11
		return selectlines[26]

	def SetParameterizationForVegetationFunction(name):
		if name == "Raupach_BLM1994" or name == "CM_QJRMS1998" or name == "vegTypeTable":
			pass
		else:
			print("Check your input at (17) SetParameterizationForVegetationFunction !! ")
		selectlines[27] = 'veg_traits                      %s            ! (17) choice of parameterization for vegetation roughness length and displacement height \n' % name
		return selectlines[27]

	def SetParameterizationForCanopyEmissivityFunction(name):
		if name == "simplExp" or name == "difTrans":
			pass
		else:
			print("Check your input at (18) SetParameterizationForCanopyEmissivityFunction !! ")
		selectlines[28] = 'canopyEmis                      %s            ! (18) choice of parameterization for canopy emissivity \n' % name
		return selectlines[28]

	def SetParameterizationForSnowInterceptionFunction(name):
		if name == "stickySnow" or name == "lightSnow" :
			pass
		else:
			print("Check your input at (19) SetParameterizationForSnowInterceptionFunction !! ")
		selectlines[29] = 'snowIncept                      %s            ! (19) choice of parameterization for snow interception \n' % name
		return selectlines[29]

	def SetWindProfileFunction(name):
		if name == "exponential" or name == "logBelowCanopy":
			pass
		else:
			print("Check your input at (20) SetWindProfileFunction !! ")
		selectlines[30] = 'windPrfile                      %s            ! (20) choice of wind profile through the canopy \n' % name
		return selectlines[30]

	def SetStabilityFunction(name):
		if name == "standard" or name == "louisinv" or name == "mahrtexp":
			pass
		else:
			print("Check your input at (21) SetStabilityFunction !! ")
		selectlines[31] = 'astability                      %s            ! (21) choice of stability function \n' % name
		return selectlines[31]

	def SetCanopyShortwaveRadiationMethodFunction(name):
		if name == "noah_mp" or name == "CLM_2stream" or name == "UEB_2stream" or name == "NL_scatter" or name == "BeersLaw":
			pass
		else:
			print("Check your input at (22) SetCanopyShortwaveRadiationMethodFunction !! ")
		selectlines[32] = 'canopySrad                      %s            ! (22) choice of canopy shortwave radiation method \n' % name
		return selectlines[32]

	def SetAlbedoRepresentationFunction(name):
		if name == "conDecay" or name == "varDecay":
			pass
		else:
			print("Check your input at (23) SetAlbedoRepresentationFunction !! ")
		selectlines[33] = 'alb_method                      %s            ! (23) choice of albedo representation \n' % name
		return selectlines[33]

	def SetCompactionRoutineFunction(name):
		if name == "consettl" or name == "anderson" :
			pass
		else:
			print("Check your input at (24) SetCompactionRoutineFunction !! ")
		selectlines[34] = 'compaction                      %s            ! (24) choice of compaction routine \n' % name
		return selectlines[34]

	def SetSnowLayersFunction(name):
		if name == "CLM_2010" or name == "jrdn1991":
			pass
		else:
			print("Check your input at (25) SetSnowLayersFunction !! ")
		selectlines[35] = 'snowLayers                      %s            ! (25) choice of method to combine and sub-divide snow layers \n' % name
		return selectlines[35]

	def SetThermalConductivityRepresentationForSnowFunction(name):
		if name == "tyen1965" or name == "melr1977" or name == "jrdn1991" or name == "smnv2000":
			pass
		else:
			print("Check your input at (26) SetThermalConductivityRepresentationForSnowFunction !! ")
		selectlines[36] = 'thCondSnow                      %s            ! (26) choice of thermal conductivity representation for snow \n' % name
		return selectlines[36]

	def SetThermalConductivityRepresentationForSoilFunction(name):
		if name == "funcSoilWet" or name == "mixConstit" or name == "hanssonVZJ":
			pass
		else:
			print("Check your input at (27) SetThermalConductivityRepresentationForSoilFunction !! ")
		selectlines[37] = 'thCondSoil                      %s            ! (27) choice of thermal conductivity representation for soil \n' % name
		return selectlines[37]

	def SetSpatialRepresentationOfGroundwaterFunction(name):
		if name == "localColumn" or name == "singleBasin":
			pass
		else:
			print("Check your input at (28) SetSpatialRepresentationOfGroundwaterFunction !! ")
		if name28 == 'singleBasin':
			if name11 == "bigBuckt":
				pass
			else:
				print("You selected '%s' at (11) SetGroundwaterRarameterizationFunction.\n"
					  "'bigBuckt' must be selected (11) SetGroundwaterRarameterizationFunction when using 'singleBasin' at (28) SetSpatialRepresentationOfGroundwaterFunction" %name11)
		selectlines[38] = 'spatial_gw                      %s            ! (28) choice of method for the spatial representation of groundwater \n' % name
		return selectlines[38]

	def SetSubGridRoutingFunction(name):
		if name == "timeDlay" or name == "qInstant":
			pass
		else:
			print("Check your input at (29) SetSubGridRoutingFunction !! ")
		selectlines[39] = 'subRouting                      %s            ! (29) choice of method for sub-grid routing \n' % name
		return selectlines[39]

	def EditSave(self):
		filepath = self.path + self.filename
		fileopen = open(filepath, 'wt')
		for line in selectlines:
			fileopen.write(line)


Decisionfile = Decisions("D:\\pysumma\\pysumma_alpha\\pysumma\\pysumma\\pysumma\\", "Decision.txt")
selectlines = Decisionfile.OpenRead()


print("Date input format : (ex) YYYY-MM-DD HH:MM")
StartDate = input("(01) simulation start time : ")
Decisions.SetStartDateFunction(StartDate)

print("Date input format : (ex) YYYY-MM-DD HH:MM")
EndDate = input("(02) simulation end time : ")
Decisions.SetEndDateFunction(EndDate)

name3 = input("(03) Select STAS or STAS-RUC or ROSETTA : ")
Decisions.SetSoilCategoryDatasetFunction(name3)

name4 = input("(04) Select USGS or MODIFIED_IGBP_MODIS_NOAH : ")
Decisions.SetVegetationCategoryDatasetFunction(name4)

name5 = input("(05) Select NoahType or CLM_Type or SiB_Type : ")
Decisions.SetSoilMoistureControlFunction(name5)

name6 = input("(06) Select BallBerry or Jarvis : ")
Decisions.SetStomatalResistanceFunction(name6)

name7 = input("(07) Select itertive or non_iter or itersurf : ")
Decisions.SetNumericalMethodFunction(name7)

name8 = input("(08) Select numericl or analytic : ")
Decisions.SetFluxDerivativesFunction(name8)

name9 = input("(09) Select monTable or specified : ")
Decisions.SetLAIandSAIFunction(name9)

name10 = input("(10) Select moisture or mixdform : ")
Decisions.SetRichardsEquationFunction(name10)

name11 = input("(11) Select qTopmodl or bigBuckt or noXplict : ")
Decisions.SetGroundwaterRarameterizationFunction(name11)

name12 = input("(12) Select constant or pow_prof : ")
Decisions.SetHydraulicConductivityProfileFunction(name12)

name13 = input("(13) Select presTemp or nrg_flux : ")
Decisions.SetUpperBoundaryConditionsForThermodynamicsFunction(name13)

name14 = input("(14) Select presTemp or zeroFlux : ")
Decisions.SetLowerBoundaryConditionsForThermodynamicsFunction(name14)

name15 = input("(15) Select presHead or liq_flux : ")
Decisions.SetUpperBoundaryConditionsForSoilHydrologyFunction(name15)

name16 = input("(16) Select drainage or presHead or bottmPsi or zeroFlux : ")
Decisions.SetLowerBoundaryConditionsForSoilHydrologyFunction(name16)

name17 = input("(17) Select Raupach_BLM1994 or CM_QJRMS1998 or vegTypeTable : ")
Decisions.SetParameterizationForVegetationFunction(name17)

name18 = input("(18) Select simplExp or difTrans : ")
Decisions.SetParameterizationForCanopyEmissivityFunction(name18)

name19 = input("(19) Select stickySnow or lightSnow : ")
Decisions.SetParameterizationForSnowInterceptionFunction(name19)

name20 = input("(20) Select exponential or logBelowCanopy : ")
Decisions.SetWindProfileFunction(name20)

name21 = input("(21) Select standard or louisinv or mahrtexp : ")
Decisions.SetStabilityFunction(name21)

name22 = input("(22) Select noah_mp or CLM_2stream or UEB_2stream or NL_scatter or BeersLaw : ")
Decisions.SetCanopyShortwaveRadiationMethodFunction(name22)

name23 = input("(23) Select conDecay or varDecay : ")
Decisions.SetAlbedoRepresentationFunction(name23)

name24 = input("(24) Select consettl or anderson : ")
Decisions.SetCompactionRoutineFunction(name24)

name25 = input("(25) Select CLM_2010 or jrdn1991 : ")
Decisions.SetSnowLayersFunction(name25)

name26 = input("(26) Select tyen1965 or melr1977 or jrdn1991 or smnv2000 : ")
Decisions.SetThermalConductivityRepresentationForSnowFunction(name26)

name27 = input("(27) Select funcSoilWet or mixConstit or hanssonVZJ : ")
Decisions.SetThermalConductivityRepresentationForSoilFunction(name27)

name28 = input("(28) Select localColumn or singleBasin : ")
Decisions.SetSpatialRepresentationOfGroundwaterFunction(name28)

name29 = input("(29) Select timeDlay or qInstant : ")
Decisions.SetSubGridRoutingFunction(name29)

Decisionfile.EditSave()


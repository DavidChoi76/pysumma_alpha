class Decisions:

	def __init__(self, path, filename):
		self.path = path
		self.filename = filename

	def OpenRead(self):
		filepath = self.path+self.filename
		fileopen = open(filepath, 'rt')
		lines = fileopen.readlines()
		return lines

	def SetStartDateFunction(name, selectlines):
		selectlines[9] = "simulStart              '%s'                   ! (01) simulation start time -- must be in single quotes \n" % name
		return selectlines[9]

	def SetEndDateFunction(name, selectlines):
		selectlines[10] = "simulFinsh             '%s'                   ! (02) simulation end time -- must be in single quotes \n" % name

	def SetSoilCategoryDatasetFunction(name, selectlines):
		if name == "STAS" or name == "STAS-RUC" or name == "ROSETTA":
			pass
		else:
			print("Check your input at (03) SetStomatalResistanceFunction !! ")
		selectlines[12] = 'soilCatTbl                      %s            ! (03) soil-category dateset \n' % name
		return selectlines[12]

	def SetVegetationCategoryDatasetFunction(name, selectlines):
		if name == "USGS" or name == "MODIFIED_IGBP_MODIS_NOAH":
			pass
		else:
			print("Check your input at (04) SetStomatalResistanceFunction !! ")
		selectlines[13] = 'vegeParTbl                      %s            ! (04) vegetation category dataset \n' % name
		return selectlines[13]

	def SetSoilMoistureControlFunction(name, selectlines):
		if name == "NoahType" or name == "CLM_Type" or name == "SiB_Type":
			pass
		else:
			print("Check your input at (05) SetSoilCategoryDatasetFunction !! ")
		selectlines[14] = 'soilStress                      %s            ! (05) choice of function for the soil moisture control on stomatal resistance \n' % name
		return selectlines[14]

	def SetStomatalResistanceFunction(name, selectlines):
		if name == "BallBerry" or name == "Jarvis":
			pass
		else:
			print("Check your input at (06) SetStomatalResistanceFunction !! ")
		selectlines[15] = 'stomResist                      %s            ! (06) choice of function for stomatal resistance \n' % name
		return selectlines[15]

	def SetNumericalMethodFunction(name, selectlines):
		if name == "itertive" or name == "non_iter" or name == "itersurf":
			pass
		else:
			print("Check your input at (07) SetNumericalMethodFunction !! ")
		selectlines[17] = 'num_method                      %s            ! (07) choice of numerical method \n' % name
		return selectlines[17]

	def SetFluxDerivativesFunction(name, selectlines):
		if name == "numericl" or name == "analytic":
			pass
		else:
			print("Check your input at (08) SetFluxDerivativesFunction !! ")
		selectlines[18] = 'fDerivMeth                      %s            ! (08) method used to calculate flux derivatives \n' % name
		return selectlines[18]

	def SetLAIandSAIFunction(name, selectlines):
		if name == "monTable" or name == "specified":
			pass
		else:
			print("Check your input at (09) SetLAIandSAIFunction !! ")
		if (name == 'specified'):
			print("LAI and SAI method option ['specified'] is no longer supported !! ")
		selectlines[19] = 'LAI_method                      %s            ! (09) method used to determine LAI and SAI \n' % name
		return selectlines[19]

	def SetRichardsEquationFunction(name, selectlines):
		if name == "moisture" or name == "mixdform":
			pass
		else:
			print("Check your input at (10) SetRichardsEquationFunction !! ")
		selectlines[20] = 'f_Richards                      %s            ! (10) form of Richards equation \n' % name
		return selectlines[20]

	def SetGroundwaterRarameterizationFunction(name, selectlines):
		if name == "qTopmodl" or name == "bigBuckt" or name == "noXplict":
			pass
		else:
			print("Check your input at (11) SetGroundwaterRarameterizationFunction !! ")
		if (name == 'qTopmodl'):
			print("you selected 'qTopmodl'. Therefore you have to select 'zeroFlux' at (16) SetLowerBoundaryConditionsForSoilHydrologyFunction !! ")
		selectlines[21] = 'groundwatr                      %s            ! (11) choice of groundwater parameterization \n' % name
		return selectlines[21]

	def SetHydraulicConductivityProfileFunction(name, name11, selectlines):
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

	def SetUpperBoundaryConditionsForThermodynamicsFunction(name, selectlines):
		if name == "presTemp" or name == "nrg_flux":
			pass
		else:
			print("Check your input at (13) SetUpperBoundaryConditionsForThermodynamicsFunction !! ")
		if (name == 'presTemp'):
			print("you selected 'presTemp'. Therefore you have to select 'presHead' at (15) SetUpperBoundaryConditionsForSoilHydrologyFunction and (16) SetLowerBoundaryConditionsForSoilHydrologyFunction !! ")

		selectlines[23] = 'bcUpprTdyn                      %s            ! (13) type of upper boundary condition for thermodynamics \n' % name
		return selectlines[23]

	def SetLowerBoundaryConditionsForThermodynamicsFunction(name, selectlines):
		if name == "presTemp" or name == "zeroFlux":
			pass
		else:
			print("Check your input at (14) SetLowerBoundaryConditionsForThermodynamicsFunction !! ")
		selectlines[24] = 'bcLowrTdyn                      %s            ! (14) type of lower boundary condition for thermodynamics \n' % name
		return selectlines[24]

	def SetUpperBoundaryConditionsForSoilHydrologyFunction(name, name13, name14, selectlines):
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

	def SetLowerBoundaryConditionsForSoilHydrologyFunction(name, name13, name14, selectlines):
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

	def SetParameterizationForVegetationFunction(name, selectlines):
		if name == "Raupach_BLM1994" or name == "CM_QJRMS1998" or name == "vegTypeTable":
			pass
		else:
			print("Check your input at (17) SetParameterizationForVegetationFunction !! ")
		selectlines[27] = 'veg_traits                      %s            ! (17) choice of parameterization for vegetation roughness length and displacement height \n' % name
		return selectlines[27]

	def SetParameterizationForCanopyEmissivityFunction(name, selectlines):
		if name == "simplExp" or name == "difTrans":
			pass
		else:
			print("Check your input at (18) SetParameterizationForCanopyEmissivityFunction !! ")
		selectlines[28] = 'canopyEmis                      %s            ! (18) choice of parameterization for canopy emissivity \n' % name
		return selectlines[28]

	def SetParameterizationForSnowInterceptionFunction(name, selectlines):
		if name == "stickySnow" or name == "lightSnow" :
			pass
		else:
			print("Check your input at (19) SetParameterizationForSnowInterceptionFunction !! ")
		selectlines[29] = 'snowIncept                      %s            ! (19) choice of parameterization for snow interception \n' % name
		return selectlines[29]

	def SetWindProfileFunction(name, selectlines):
		if name == "exponential" or name == "logBelowCanopy":
			pass
		else:
			print("Check your input at (20) SetWindProfileFunction !! ")
		selectlines[30] = 'windPrfile                      %s            ! (20) choice of wind profile through the canopy \n' % name
		return selectlines[30]

	def SetStabilityFunction(name, selectlines):
		if name == "standard" or name == "louisinv" or name == "mahrtexp":
			pass
		else:
			print("Check your input at (21) SetStabilityFunction !! ")
		selectlines[31] = 'astability                      %s            ! (21) choice of stability function \n' % name
		return selectlines[31]

	def SetCanopyShortwaveRadiationMethodFunction(name, selectlines):
		if name == "noah_mp" or name == "CLM_2stream" or name == "UEB_2stream" or name == "NL_scatter" or name == "BeersLaw":
			pass
		else:
			print("Check your input at (22) SetCanopyShortwaveRadiationMethodFunction !! ")
		selectlines[32] = 'canopySrad                      %s            ! (22) choice of canopy shortwave radiation method \n' % name
		return selectlines[32]

	def SetAlbedoRepresentationFunction(name, selectlines):
		if name == "conDecay" or name == "varDecay":
			pass
		else:
			print("Check your input at (23) SetAlbedoRepresentationFunction !! ")
		selectlines[33] = 'alb_method                      %s            ! (23) choice of albedo representation \n' % name
		return selectlines[33]

	def SetCompactionRoutineFunction(name, selectlines):
		if name == "consettl" or name == "anderson" :
			pass
		else:
			print("Check your input at (24) SetCompactionRoutineFunction !! ")
		selectlines[34] = 'compaction                      %s            ! (24) choice of compaction routine \n' % name
		return selectlines[34]

	def SetSnowLayersFunction(name, selectlines):
		if name == "CLM_2010" or name == "jrdn1991":
			pass
		else:
			print("Check your input at (25) SetSnowLayersFunction !! ")
		selectlines[35] = 'snowLayers                      %s            ! (25) choice of method to combine and sub-divide snow layers \n' % name
		return selectlines[35]

	def SetThermalConductivityRepresentationForSnowFunction(name, selectlines):
		if name == "tyen1965" or name == "melr1977" or name == "jrdn1991" or name == "smnv2000":
			pass
		else:
			print("Check your input at (26) SetThermalConductivityRepresentationForSnowFunction !! ")
		selectlines[36] = 'thCondSnow                      %s            ! (26) choice of thermal conductivity representation for snow \n' % name
		return selectlines[36]

	def SetThermalConductivityRepresentationForSoilFunction(name, selectlines):
		if name == "funcSoilWet" or name == "mixConstit" or name == "hanssonVZJ":
			pass
		else:
			print("Check your input at (27) SetThermalConductivityRepresentationForSoilFunction !! ")
		selectlines[37] = 'thCondSoil                      %s            ! (27) choice of thermal conductivity representation for soil \n' % name
		return selectlines[37]

	def SetSpatialRepresentationOfGroundwaterFunction(name, name11, selectlines):
		if name == "localColumn" or name == "singleBasin":
			pass
		else:
			print("Check your input at (28) SetSpatialRepresentationOfGroundwaterFunction !! ")
		if name == 'singleBasin':
			if name11 == "bigBuckt":
				pass
			else:
				print("You selected '%s' at (11) SetGroundwaterRarameterizationFunction.\n"
					  "'bigBuckt' must be selected (11) SetGroundwaterRarameterizationFunction when using 'singleBasin' at (28) SetSpatialRepresentationOfGroundwaterFunction" %name11)
		selectlines[38] = 'spatial_gw                      %s            ! (28) choice of method for the spatial representation of groundwater \n' % name
		return selectlines[38]

	def SetSubGridRoutingFunction(name, selectlines):
		if name == "timeDlay" or name == "qInstant":
			pass
		else:
			print("Check your input at (29) SetSubGridRoutingFunction !! ")
		selectlines[39] = 'subRouting                      %s            ! (29) choice of method for sub-grid routing \n' % name
		return selectlines[39]

	def EditSave(self, selectlines):
		filepath = self.path + self.filename
		fileopen = open(filepath, 'wt')
		for line in selectlines:
			fileopen.write(line)
		return line
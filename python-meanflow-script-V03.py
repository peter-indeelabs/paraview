#Program Description:
#This script automate post-processing images for meanflow field from Paraview
#Author: Fong Pan (Peter), Indeelabs
#Version: Revion-03
#Date: Oct 27, 2019

from paraview.simple import *

#----------------
#User Input parameters

workdir='/home/fong/Downloads/sim18-pimpleSoMeanflowEnsight/'
lineBegin=-0.001
lineEnd=0.001

#----------------

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'EnSight Reader'
filecasename=workdir+'shared.case'
sharedcase = EnSightReader(CaseFileName=filecasename)
sharedcase.CellArrays = ['pMean', 'pPrime2Mean', 'Q', 'QMean', 'p', 'U', 'UMean', 'vorticityMean', 'vorticity', 'UPrime2Mean']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [701, 736]

# get color transfer function/color map for 'pMean'
pMeanLUT = GetColorTransferFunction('pMean')

# get opacity transfer function/opacity map for 'pMean'
pMeanPWF = GetOpacityTransferFunction('pMean')

# show data in view
sharedcaseDisplay = Show(sharedcase, renderView1)
# trace defaults for the display properties.
sharedcaseDisplay.Representation = 'Surface'
sharedcaseDisplay.ColorArrayName = ['CELLS', 'pMean']
sharedcaseDisplay.LookupTable = pMeanLUT
sharedcaseDisplay.OSPRayScaleArray = 'pMean'
sharedcaseDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sharedcaseDisplay.SelectOrientationVectors = 'U'
sharedcaseDisplay.ScaleFactor = 0.000829496467486024
sharedcaseDisplay.SelectScaleArray = 'pMean'
sharedcaseDisplay.GlyphType = 'Arrow'
sharedcaseDisplay.GlyphTableIndexArray = 'pMean'
sharedcaseDisplay.DataAxesGrid = 'GridAxesRepresentation'
sharedcaseDisplay.PolarAxes = 'PolarAxesRepresentation'
sharedcaseDisplay.ScalarOpacityFunction = pMeanPWF
sharedcaseDisplay.ScalarOpacityUnitDistance = 2.370430515134391e-05

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
sharedcaseDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=sharedcase)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, -2e-05]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'pMean']
slice1Display.LookupTable = pMeanLUT
slice1Display.OSPRayScaleArray = 'pMean'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.0008294890634715558
slice1Display.SelectScaleArray = 'pMean'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'pMean'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(sharedcase, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(sharedcase)

# set active source
SetActiveSource(slice1)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Calculator'
calculator1 = Calculator(Input=slice1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.AttributeMode = 'Cell Data'
calculator1.ResultArrayName = 'PmeanPSI'
calculator1.Function = 'pMean*0.000145038*1011.4+14.7'

# get color transfer function/color map for 'PmeanPSI'
pmeanPSILUT = GetColorTransferFunction('PmeanPSI')

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['CELLS', 'PmeanPSI']
calculator1Display.LookupTable = pmeanPSILUT
calculator1Display.OSPRayScaleArray = 'PmeanPSI'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U'
calculator1Display.ScaleFactor = 0.0008294890634715558
calculator1Display.SelectScaleArray = 'PmeanPSI'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'PmeanPSI'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(calculator1)

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display = Show(calculator1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# get opacity transfer function/opacity map for 'PmeanPSI'
pmeanPSIPWF = GetOpacityTransferFunction('PmeanPSI')

# Rescale transfer function
pmeanPSIPWF.RescaleTransferFunction(0.0, 135.0)


# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pmeanPSILUT.ApplyPreset('jet', True)

# get color legend/bar for pmeanPSILUT in view renderView1
pmeanPSILUTColorBar = GetScalarBar(pmeanPSILUT, renderView1)

# Properties modified on pmeanPSILUTColorBar
pmeanPSILUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# change scalar bar placement
pmeanPSILUTColorBar.Orientation = 'Horizontal'
pmeanPSILUTColorBar.WindowLocation = 'AnyLocation'
pmeanPSILUTColorBar.Position = [0.31, 0.073]

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0
# update the view to ensure updated data information
renderView1.Update()

# Properties modified on pmeanPSILUTColorBar
pmeanPSILUTColorBar.Title = 'Meanflow Absolute Pressure [Psia]'
pmeanPSILUTColorBar.ScalarBarLength = 0.15

pmeanPSILUTColorBar.ScalarBarLength = 0.15
pmeanPSILUTColorBar.ScalarBarThickness = 8
pmeanPSILUTColorBar.TitleFontSize = 5
pmeanPSILUTColorBar.LabelFontSize = 5
pmeanPSILUTColorBar.LabelColor = [0.0, 0.0, 0.0]
pmeanPSILUTColorBar.TitleBold = 1
pmeanPSILUTColorBar.LabelBold = 1
pmeanPSILUTColorBar.TitleColor = [0.0, 0.0, 0.0]
pmeanPSILUTColorBar.UseCustomLabels = 1
pmeanPSILUTColorBar.CustomLabels = [15,35,55,76,95,115,135]
pmeanPSILUTColorBar.RangeLabelFormat = '%3.0f'
pmeanPSILUTColorBar.AddRangeLabels = 1
pmeanPSILUTColorBar.DrawTickMarks = 1

#### saving camera placements for all active views

# current camera placement for renderView1

renderView1.CameraPosition = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.019043749135980843]
renderView1.CameraFocalPoint = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]
renderView1.CameraParallelScale = 0.001212764330427908
renderView1.CameraParallelProjection = 1


#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

filename=workdir+'img-meanPressure.png'
SaveAnimation(filename, renderView1, ImageResolution=[1097, 736], FrameWindow=[0, 0])


#Step 2: Meanflow Ux
# find source
calculator1 = FindSource('Calculator1')

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.Function = ''

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
slice1 = FindSource('Slice1')

# Properties modified on calculator2
calculator2.AttributeMode = 'Cell Data'
calculator2.ResultArrayName = 'Uxmean'
calculator2.Function = '-UMean_X'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [552, 736]

# get color transfer function/color map for 'Uxmean'
uxmeanLUT = GetColorTransferFunction('Uxmean')

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['CELLS', 'Uxmean']
calculator2Display.LookupTable = uxmeanLUT
calculator2Display.OSPRayScaleArray = 'Uxmean'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'U'
calculator2Display.ScaleFactor = 0.0008294890634715558
calculator2Display.SelectScaleArray = 'Uxmean'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'Uxmean'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator1)

# get color transfer function/color map for 'PmeanPSI'
pmeanPSILUT = GetColorTransferFunction('PmeanPSI')

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['CELLS', 'PmeanPSI']
calculator1Display.LookupTable = pmeanPSILUT
calculator1Display.OSPRayScaleArray = 'PmeanPSI'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'U'
calculator1Display.ScaleFactor = 0.0008294890634715558
calculator1Display.SelectScaleArray = 'PmeanPSI'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'PmeanPSI'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(calculator2)

# get color legend/bar for uxmeanLUT in view renderView1
uxmeanLUTColorBar = GetScalarBar(uxmeanLUT, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
uxmeanLUT.RescaleTransferFunction(0.0, 20.0)

# get opacity transfer function/opacity map for 'Uxmean'
uxmeanPWF = GetOpacityTransferFunction('Uxmean')

# Rescale transfer function
uxmeanPWF.RescaleTransferFunction(0.0, 20.0)

# change scalar bar placement
uxmeanLUTColorBar.Title = 'Meanflow X-component Streamwise Velocity [m/s]'
uxmeanLUTColorBar.Orientation = 'Horizontal'
uxmeanLUTColorBar.WindowLocation = 'AnyLocation'
uxmeanLUTColorBar.Position = [0.31, 0.073]
uxmeanLUTColorBar.ScalarBarLength = 0.15


uxmeanLUTColorBar.ScalarBarLength = 0.15
uxmeanLUTColorBar.ScalarBarThickness = 8
uxmeanLUTColorBar.TitleFontSize = 5
uxmeanLUTColorBar.LabelFontSize = 5
uxmeanLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
uxmeanLUTColorBar.TitleBold = 1
uxmeanLUTColorBar.LabelBold = 1
uxmeanLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
uxmeanLUTColorBar.UseCustomLabels = 1
uxmeanLUTColorBar.CustomLabels = [0,5,10,15,20]
uxmeanLUTColorBar.RangeLabelFormat = '%3.0f'
uxmeanLUTColorBar.AddRangeLabels = 1
uxmeanLUTColorBar.DrawTickMarks = 1


# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
uxmeanLUT.ApplyPreset('jet', True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.019043749135980843]
renderView1.CameraFocalPoint = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]
renderView1.CameraParallelScale = 0.001212764330427908
renderView1.CameraParallelProjection = 1



#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

filename=workdir+'img-meanUx.png'
SaveAnimation(filename, renderView1, ImageResolution=[1097, 736], FrameWindow=[0, 0])

# Step 3: plot lines
# find source
calculator2 = FindSource('Calculator2')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=calculator2, Source='High Resolution Line Source')
plotOverLine1.Tolerance = 2.22044604925031e-16

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-0.0041474648751318455, -0.0004799999878741801, -2.0000001313746907e-05]
plotOverLine1.Source.Point2 = [0.004147425759583712, 0.00048000007518567145, -1.9999995856778696e-05]

# find source
enSightReader1 = FindSource('EnSightReader1')

# find source
slice1 = FindSource('Slice1')

# find source
calculator1 = FindSource('Calculator1')

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [lineBegin, 3e-05, -2e-05]
plotOverLine1.Source.Point2 = [lineEnd, 3e-05, -2e-05]
plotOverLine1.Source.Resolution = 1500

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [948, 736]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)
# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.OSPRayScaleArray = 'PmeanPSI'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 0.00020000000949949026
plotOverLine1Display.SelectScaleArray = 'None'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'None'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [469, 736]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, lineChartView1)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)
# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['PmeanPSI', 'pPrime2Mean', 'UMean_Magnitude', 'UPrime2Mean_Magnitude', 'Uxmean']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'p', 'p', 'pMean', 'pMean', 'PmeanPSI', 'PmeanPSI', 'pPrime2Mean', 'pPrime2Mean', 'Q', 'Q', 'QMean', 'QMean', 'U_X', 'U_X', 'U_Y', 'U_Y', 'U_Z', 'U_Z', 'U_Magnitude', 'U_Magnitude', 'UMean_X', 'UMean_X', 'UMean_Y', 'UMean_Y', 'UMean_Z', 'UMean_Z', 'UMean_Magnitude', 'UMean_Magnitude', 'UPrime2Mean_XX', 'UPrime2Mean_XX', 'UPrime2Mean_YY', 'UPrime2Mean_YY', 'UPrime2Mean_ZZ', 'UPrime2Mean_ZZ', 'UPrime2Mean_XY', 'UPrime2Mean_XY', 'UPrime2Mean_YZ', 'UPrime2Mean_YZ', 'UPrime2Mean_XZ', 'UPrime2Mean_XZ', 'UPrime2Mean_Magnitude', 'UPrime2Mean_Magnitude', 'Uxmean', 'Uxmean', 'vorticity_X', 'vorticity_X', 'vorticity_Y', 'vorticity_Y', 'vorticity_Z', 'vorticity_Z', 'vorticity_Magnitude', 'vorticity_Magnitude', 'vorticityMean_X', 'vorticityMean_X', 'vorticityMean_Y', 'vorticityMean_Y', 'vorticityMean_Z', 'vorticityMean_Z', 'vorticityMean_Magnitude', 'vorticityMean_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'p', '0.89', '0.1', '0.11', 'pMean', '0.22', '0.49', '0.72', 'PmeanPSI', '0.3', '0.69', '0.29', 'pPrime2Mean', '0.6', '0.31', '0.64', 'Q', '1', '0.5', '0', 'QMean', '0.65', '0.34', '0.16', 'U_X', '0', '0', '0', 'U_Y', '0.89', '0.1', '0.11', 'U_Z', '0.22', '0.49', '0.72', 'U_Magnitude', '0.3', '0.69', '0.29', 'UMean_X', '0.6', '0.31', '0.64', 'UMean_Y', '1', '0.5', '0', 'UMean_Z', '0.65', '0.34', '0.16', 'UMean_Magnitude', '0', '0', '0', 'UPrime2Mean_XX', '0.89', '0.1', '0.11', 'UPrime2Mean_YY', '0.22', '0.49', '0.72', 'UPrime2Mean_ZZ', '0.3', '0.69', '0.29', 'UPrime2Mean_XY', '0.6', '0.31', '0.64', 'UPrime2Mean_YZ', '1', '0.5', '0', 'UPrime2Mean_XZ', '0.65', '0.34', '0.16', 'UPrime2Mean_Magnitude', '0', '0', '0', 'Uxmean', '0.89', '0.1', '0.11', 'vorticity_X', '0.22', '0.49', '0.72', 'vorticity_Y', '0.3', '0.69', '0.29', 'vorticity_Z', '0.6', '0.31', '0.64', 'vorticity_Magnitude', '1', '0.5', '0', 'vorticityMean_X', '0.65', '0.34', '0.16', 'vorticityMean_Y', '0', '0', '0', 'vorticityMean_Z', '0.89', '0.1', '0.11', 'vorticityMean_Magnitude', '0.22', '0.49', '0.72', 'vtkValidPointMask', '0.3', '0.69', '0.29', 'Points_X', '0.6', '0.31', '0.64', 'Points_Y', '1', '0.5', '0', 'Points_Z', '0.65', '0.34', '0.16', 'Points_Magnitude', '0', '0', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'p', '0', 'pMean', '0', 'PmeanPSI', '0', 'pPrime2Mean', '0', 'Q', '0', 'QMean', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UMean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_ZZ', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_Magnitude', '0', 'Uxmean', '0', 'vorticity_X', '0', 'vorticity_Y', '0', 'vorticity_Z', '0', 'vorticity_Magnitude', '0', 'vorticityMean_X', '0', 'vorticityMean_Y', '0', 'vorticityMean_Z', '0', 'vorticityMean_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'p', '1', 'pMean', '1', 'PmeanPSI', '1', 'pPrime2Mean', '1', 'Q', '1', 'QMean', '1', 'U_X', '1', 'U_Y', '1', 'U_Z', '1', 'U_Magnitude', '1', 'UMean_X', '1', 'UMean_Y', '1', 'UMean_Z', '1', 'UMean_Magnitude', '1', 'UPrime2Mean_XX', '1', 'UPrime2Mean_YY', '1', 'UPrime2Mean_ZZ', '1', 'UPrime2Mean_XY', '1', 'UPrime2Mean_YZ', '1', 'UPrime2Mean_XZ', '1', 'UPrime2Mean_Magnitude', '1', 'Uxmean', '1', 'vorticity_X', '1', 'vorticity_Y', '1', 'vorticity_Z', '1', 'vorticity_Magnitude', '1', 'vorticityMean_X', '1', 'vorticityMean_Y', '1', 'vorticityMean_Z', '1', 'vorticityMean_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'p', '2', 'pMean', '2', 'PmeanPSI', '2', 'pPrime2Mean', '2', 'Q', '2', 'QMean', '2', 'U_X', '2', 'U_Y', '2', 'U_Z', '2', 'U_Magnitude', '2', 'UMean_X', '2', 'UMean_Y', '2', 'UMean_Z', '2', 'UMean_Magnitude', '2', 'UPrime2Mean_XX', '2', 'UPrime2Mean_YY', '2', 'UPrime2Mean_ZZ', '2', 'UPrime2Mean_XY', '2', 'UPrime2Mean_YZ', '2', 'UPrime2Mean_XZ', '2', 'UPrime2Mean_Magnitude', '2', 'Uxmean', '2', 'vorticity_X', '2', 'vorticity_Y', '2', 'vorticity_Z', '2', 'vorticity_Magnitude', '2', 'vorticityMean_X', '2', 'vorticityMean_Y', '2', 'vorticityMean_Z', '2', 'vorticityMean_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'p', '0', 'pMean', '0', 'PmeanPSI', '0', 'pPrime2Mean', '0', 'Q', '0', 'QMean', '0', 'U_X', '0', 'U_Y', '0', 'U_Z', '0', 'U_Magnitude', '0', 'UMean_X', '0', 'UMean_Y', '0', 'UMean_Z', '0', 'UMean_Magnitude', '0', 'UPrime2Mean_XX', '0', 'UPrime2Mean_YY', '0', 'UPrime2Mean_ZZ', '0', 'UPrime2Mean_XY', '0', 'UPrime2Mean_YZ', '0', 'UPrime2Mean_XZ', '0', 'UPrime2Mean_Magnitude', '0', 'Uxmean', '0', 'vorticity_X', '0', 'vorticity_Y', '0', 'vorticity_Z', '0', 'vorticity_Magnitude', '0', 'vorticityMean_X', '0', 'vorticityMean_Y', '0', 'vorticityMean_Z', '0', 'vorticityMean_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# save data
SaveData(workdir+'data-plotline.csv', proxy=plotOverLine1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.019043749135980843]
renderView1.CameraFocalPoint = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]
renderView1.CameraParallelScale = 0.0017756082561795003
renderView1.CameraParallelProjection = 1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).


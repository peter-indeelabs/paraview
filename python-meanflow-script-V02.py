from paraview.simple import *

#----------------
#Input parameters

workdir='/home/fong/Downloads/sim18-pimpleSoMeanflowEnsight/'


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

filename=workdir+'/img-meanPressure.png'
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

filename=workdir+'/img-meanUx.png'
SaveAnimation(filename, renderView1, ImageResolution=[1097, 736], FrameWindow=[0, 0])


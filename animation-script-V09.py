#Program Description:
#This script automate post-processing images and video for transient flow field from Paraview
#Author: Fong Pan (Peter), Indeelabs
#Version: Revion-09
#Date: Oct 27, 2019

#-----------------------------------------------
#### import the simple module from the paraview
from paraview.simple import *

##---------------------------------------------------
#input parameters
startFrame=0
endFrame=3
set_animation=1 #0 no animation, 1 with animation ON
workdir='/home/fong/Downloads/doetemplatepimple-makeanimation'
simTitle='sim18-600um pitch'
##---------------------------------------------------

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

filename=workdir+'/case.foam'
# create a new 'OpenFOAMReader'
#casefoam = OpenFOAMReader(FileName='/home/fong/Downloads/doetemplatepimple-makeanimation/case.foam')
casefoam = OpenFOAMReader(FileName=filename)
casefoam.MeshRegions = ['internalMesh']
casefoam.CellArrays = ['Q', 'U', 'p', 'vorticity']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [701, 736]

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# show data in view
casefoamDisplay = Show(casefoam, renderView1)
# trace defaults for the display properties.
casefoamDisplay.Representation = 'Surface'
casefoamDisplay.ColorArrayName = ['POINTS', 'p']
casefoamDisplay.LookupTable = pLUT
casefoamDisplay.OSPRayScaleArray = 'p'
casefoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
casefoamDisplay.SelectOrientationVectors = 'U'
casefoamDisplay.ScaleFactor = 0.000829496467486024
casefoamDisplay.SelectScaleArray = 'p'
casefoamDisplay.GlyphType = 'Arrow'
casefoamDisplay.GlyphTableIndexArray = 'p'
casefoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
casefoamDisplay.PolarAxes = 'PolarAxesRepresentation'
casefoamDisplay.ScalarOpacityFunction = pPWF
casefoamDisplay.ScalarOpacityUnitDistance = 2.4067436771072094e-05

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
casefoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=casefoam)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]

# Properties modified on renderView1
renderView1.CameraParallelProjection = 1

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
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.0008294890634715558
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(casefoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'vorticity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vorticity'
vorticityLUT = GetColorTransferFunction('vorticity')

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'vorticity', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
slice1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(vorticityLUT, slice1Display)

# Rescale transfer function
vorticityLUT.RescaleTransferFunction(-500000.0, 500000.0)

# get opacity transfer function/opacity map for 'vorticity'
vorticityPWF = GetOpacityTransferFunction('vorticity')

# Rescale transfer function
vorticityPWF.RescaleTransferFunction(-500000.0, 500000.0)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
vorticityLUT.ApplyPreset('Cool to Warm', True)

# get color legend/bar for vorticityLUT in view renderView1
vorticityLUTColorBar = GetScalarBar(vorticityLUT, renderView1)

# Properties modified on vorticityLUTColorBar
vorticityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
vorticityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# Properties modified on vorticityLUTColorBar
vorticityLUTColorBar.AutoOrient = 0
vorticityLUTColorBar.Orientation = 'Horizontal'
vorticityLUTColorBar.Title = 'Spanwise Vorticity [1/s]'
vorticityLUTColorBar.AutomaticLabelFormat = 0


# Properties modified on vorticityLUTColorBar
vorticityLUTColorBar.LabelFormat = '%3.0f'
# change scalar bar placement
vorticityLUTColorBar.WindowLocation = 'AnyLocation'
# Properties modified on vorticityLUTColorBar
vorticityLUTColorBar.AutoOrient = 1
# Properties modified on vorticityLUTColorBar
vorticityLUTColorBar.ComponentTitle = ''
# Hide orientation axes
renderView1.OrientationAxesVisibility = 0
# Properties modified on vorticityLUTColorBar
vorticityLUTColorBar.AutoOrient = 0
# change scalar bar placement
vorticityLUTColorBar.Position = [0.31, 0.073]

# Properties modified on uLUTColorBar
vorticityLUTColorBar.ScalarBarLength = 0.15
vorticityLUTColorBar.ScalarBarThickness = 8
vorticityLUTColorBar.TitleFontSize = 5
vorticityLUTColorBar.LabelFontSize = 5

vorticityLUTColorBar.TitleBold = 1
vorticityLUTColorBar.LabelBold = 1
vorticityLUTColorBar.UseCustomLabels = 1
vorticityLUTColorBar.CustomLabels = [-500000, -250000, 0, 250000, 500000]
vorticityLUTColorBar.RangeLabelFormat = '%3.0f'
vorticityLUTColorBar.AddRangeLabels = 1
vorticityLUTColorBar.DrawTickMarks = 1

# create a new 'Text'
text1 = Text()
# Properties modified on text1
text1.Text = simTitle
# show data in view
text1Display = Show(text1, renderView1)
# update the view to ensure updated data information
renderView1.Update()
# Properties modified on text1Display
text1Display.Color = [0.0, 0.0, 0.0]
# Properties modified on text1Display
text1Display.FontSize = 12
# Properties modified on text1Display
text1Display.WindowLocation = 'AnyLocation'
# Properties modified on text1Display
text1Display.Position = [0.4, 0.85]


#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.019043749135980843]
renderView1.CameraFocalPoint = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]
renderView1.CameraParallelScale = 0.001212764330427908
renderView1.CameraParallelProjection = 1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# save animation
if set_animation==1:
	filename=workdir+'/img-vortexZ.png'
	SaveAnimation(filename, renderView1, ImageResolution=[1097, 736], FrameWindow=[startFrame, endFrame])


#Step 2:spanwise velocity
# get display properties
slice1Display = GetDisplayProperties(slice1, view=renderView1)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U', 'Magnitude'))

# get color transfer function/color map for 'vorticity'
vorticityLUT = GetColorTransferFunction('vorticity')

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vorticityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U', 'Y'))

# rescale color and/or opacity maps used to exactly fit the current data range
slice1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(uLUT, slice1Display)

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)

# Properties modified on uLUTColorBar
uLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
uLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
uLUTColorBar.AutomaticLabelFormat = 0
uLUTColorBar.LabelFormat = '%3.1f'

# Properties modified on uLUTColorBar
uLUTColorBar.AddRangeLabels = 0

# change scalar bar placement
uLUTColorBar.Orientation = 'Horizontal'
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.318, 0.084]

# Properties modified on uLUTColorBar
uLUTColorBar.ScalarBarLength = 0.15
uLUTColorBar.ScalarBarThickness = 8
uLUTColorBar.TitleFontSize = 5
uLUTColorBar.LabelFontSize = 5
uLUTColorBar.TitleBold = 1
uLUTColorBar.LabelBold = 1
uLUTColorBar.UseCustomLabels = 1
uLUTColorBar.CustomLabels = [-4.0, -2.0, 0.0, 2.0, 4.0]
uLUTColorBar.RangeLabelFormat = '%3.1f'
uLUTColorBar.AddRangeLabels = 1
uLUTColorBar.DrawTickMarks = 1

# Properties modified on uLUTColorBar
uLUTColorBar.Title = 'Spanwise Velocity [m/s]'
uLUTColorBar.ComponentTitle = ''

# Rescale transfer function
uLUT.RescaleTransferFunction(-4.0, 4.0)

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# Rescale transfer function
uPWF.RescaleTransferFunction(-4.0, 4.0)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
uLUT.ApplyPreset('jet', True)

# save animation
if set_animation==1:
	filename=workdir+'/img-Uy.png'
	SaveAnimation(filename, renderView1, ImageResolution=[1097, 736], FrameWindow=[startFrame, endFrame])

#----
#Step 3: Q-criterion
# find source
slice1 = FindSource('Slice1')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [701, 736]

# hide data in view
Hide(slice1, renderView1)

# find source
openFOAMReader1 = FindSource('OpenFOAMReader1')

# set active source
SetActiveSource(openFOAMReader1)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# Properties modified on openFOAMReader1
openFOAMReader1.MeshRegions = ['internalMesh', 'post6', 'post5', 'post4', 'post3', 'post2', 'post1']

# find source
text1 = FindSource('Text1')

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Block'
extractBlock1 = ExtractBlock(Input=openFOAMReader1)

# set active source
SetActiveSource(openFOAMReader1)

# show data in view
extractBlock1Display = Show(extractBlock1, renderView1)
# trace defaults for the display properties.
extractBlock1Display.Representation = 'Surface'
extractBlock1Display.ColorArrayName = [None, '']
extractBlock1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractBlock1Display.SelectOrientationVectors = 'None'
extractBlock1Display.ScaleFactor = -2.0000000000000002e+298
extractBlock1Display.SelectScaleArray = 'None'
extractBlock1Display.GlyphType = 'Arrow'
extractBlock1Display.GlyphTableIndexArray = 'None'
extractBlock1Display.DataAxesGrid = 'GridAxesRepresentation'
extractBlock1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(openFOAMReader1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(extractBlock1)

# Properties modified on extractBlock1
extractBlock1.BlockIndices = [2]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on extractBlock1Display
extractBlock1Display.OSPRayScaleArray = 'Q'

# set active source
SetActiveSource(openFOAMReader1)

# create a new 'Slice'
slice2 = Slice(Input=openFOAMReader1)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]

# set active source
SetActiveSource(openFOAMReader1)

# destroy slice2
Delete(slice2)
del slice2

# create a new 'Clip'
clip1 = Clip(Input=openFOAMReader1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 403.96008682250977

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [-2.0954757928848267e-09, 4.3655745685100555e-11, 0.0013049999633949483]

# Properties modified on clip1
clip1.ClipType = 'Scalar'
clip1.Scalars = ['POINTS', 'Q']
clip1.Value = 10000000000.0

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 0.0007843115134164692
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 3.180477044682731e-05

# hide data in view
Hide(openFOAMReader1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'vorticity', 'Z'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vorticity'
vorticityLUT = GetColorTransferFunction('vorticity')

# Rescale transfer function
vorticityLUT.RescaleTransferFunction(-500000.0, 500000.0)

# get opacity transfer function/opacity map for 'vorticity'
vorticityPWF = GetOpacityTransferFunction('vorticity')

# Rescale transfer function
vorticityPWF.RescaleTransferFunction(-500000.0, 500000.0)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.013596328565593906, -0.0005646186086068463, -0.010214084613934618]
renderView1.CameraFocalPoint = [-0.0010137467578974864, 1.4966355507153598e-05, -0.00017052934106537125]
renderView1.CameraViewUp = [-0.5666546679543342, -0.006332593905915772, -0.8239310563026411]
renderView1.CameraParallelScale = 0.00028786169342265696
renderView1.CameraParallelProjection = 1

# save animation
if set_animation==1:
        filename=workdir+'/img-Q.png'
        SaveAnimation(filename, renderView1, ImageResolution=[1097, 736], FrameWindow=[startFrame, endFrame])


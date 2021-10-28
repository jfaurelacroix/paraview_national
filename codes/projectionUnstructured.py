# Programmable Filter
# vtkUnstructuredGrid
# ------
numPoints = inputs[0].GetNumberOfPoints()
side = int(round(numPoints**(1./3.)))    # round() in this Python returns float type
layer = side*side
rho = inputs[0].PointData['density']     # 1D flat array
points = vtk.vtkPoints()      # create vtkPoints instance, to contain 100^2 points in the projection
proj = vtk.vtkDoubleArray(); proj.SetName('projection')   # create the projection array
for i in range(layer):        # loop through 100x100 points
    x, y = inputs[0].GetPoint(i)[0:2]
    z, column = -20., 0.
    for j in range(side):
        column += rho.GetValue(i+layer*j)
    points.InsertNextPoint(x,y,z)        # also points.InsertPoint(i,x,y,z)
    proj.InsertNextValue(column)         # add value to this point

output.SetPoints(points)                 # add points to vtkUnstructuredGrid
output.GetPointData().SetScalars(proj)   # add projection array to these points

quad = vtk.vtkQuad()               # create a cell
output.Allocate(side, side)        # allocate space for side^2 'cells'
for i in range(side-1):
    for j in range(side-1):
        quad.GetPointIds().SetId(0,i+j*side)
        quad.GetPointIds().SetId(1,(i+1)+j*side)
        quad.GetPointIds().SetId(2,(i+1)+(j+1)*side)
        quad.GetPointIds().SetId(3,i+(j+1)*side)
        output.InsertNextCell(vtk.VTK_QUAD, quad.GetPointIds())

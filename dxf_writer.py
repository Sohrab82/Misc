# documentation
# http://dxfwrite.readthedocs.io/en/latest/entities/polyline.html

from dxfwrite import DXFEngine as dxf
drawing = dxf.drawing('test.dxf')
drawing.add(dxf.line((0, 0), (10, 0), color=7))

polyline = dxf.polyline(linetype='DOT')
polyline.add_vertices([(0, 20), (3, 20), (6, 23), (9, 23)])
drawing.add(polyline)


drawing.add_layer('TEXTLAYER', color=2)
drawing.add(dxf.text('Test', insert=(0, 0.2), layer='TEXTLAYER'))
drawing.save()

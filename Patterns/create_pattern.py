import math
import svgwrite
from shapely.geometry import Point, Polygon
from cairosvg import svg2png

# Define the SVG canvas size and grid dimensions
CANVAS_SIZE = (400, 400)
GRID_SIZE = 20
LINE_WIDTH = 1

# Define the colors
BLUE = "#0000FF"
GREEN = "#00FF00"
RED = "#FF0000"

# Create the SVG object with a black background
dwg = svgwrite.Drawing(filename="test_pattern.svg", size=CANVAS_SIZE, profile='full', viewBox=f'0 0 {CANVAS_SIZE[0]} {CANVAS_SIZE[1]}')
dwg.add(dwg.rect(insert=(0,0), size=('100%', '100%'), fill='black'))

# Calculate the grid spacing
grid_spacing = math.floor(CANVAS_SIZE[0] / GRID_SIZE)

# Draw the vertical and horizontal blue lines
for i in range(GRID_SIZE + 1):
    x = i * grid_spacing
    dwg.add(dwg.line(start=(x, 0), end=(x, CANVAS_SIZE[1]), stroke=BLUE, stroke_width=LINE_WIDTH))
    y = i * grid_spacing
    dwg.add(dwg.line(start=(0, y), end=(CANVAS_SIZE[0], y), stroke=BLUE, stroke_width=LINE_WIDTH))

# Draw the center green lines
dwg.add(dwg.line(start=(0, CANVAS_SIZE[1] / 2), end=(CANVAS_SIZE[0], CANVAS_SIZE[1] / 2), stroke=GREEN, stroke_width=LINE_WIDTH))
dwg.add(dwg.line(start=(CANVAS_SIZE[0] / 2, 0), end=(CANVAS_SIZE[0] / 2, CANVAS_SIZE[1]), stroke=GREEN, stroke_width=LINE_WIDTH))

# Define the points of the triangle
p1 = (4 * grid_spacing + 5, 8 * grid_spacing + 7)
p2 = (9 * grid_spacing + 2, 14 * grid_spacing - 5)
p3 = (14 * grid_spacing -1 , 6 * grid_spacing - 12)

# Draw the blue dots at each crossing of blue lines
for i in range(1, GRID_SIZE):
    for j in range(1, GRID_SIZE):
        x = i * grid_spacing
        y = j * grid_spacing
        dot = (x, y)
        triangle_points = [p1, p2, p3]
        dotX = Point(x, y)
        triangle = Polygon(triangle_points)
        if triangle.contains(dotX) or triangle.intersects(dotX):
            dwg.add(dwg.circle(center=dot, r=4, fill=RED))
        elif dot[0] % grid_spacing == 0 or dot[1] % grid_spacing == 0:
            dwg.add(dwg.circle(center=dot, r=4, fill=BLUE))

# Draw the green triangle
dwg.add(dwg.polygon(points=[p1, p2, p3], fill="none", stroke=GREEN, stroke_width=LINE_WIDTH))

# Save the SVG file
dwg.save()


svg_code = open("test_pattern.svg", 'rt').read()
svg2png(bytestring=svg_code, write_to='redshift_triangle.png', output_width=7680, output_height=7680)
import sys
import math
import Line_Point
big_count = 0
'''
purpose
	write to stdout a dragon curve with i iterations, line length l, and colour c preconditions
	i and l are positive non-zero ints and floats (respectively)
	c is a string
'''
def next_line(root, i, turn):
	# copy root
	new_line = Line_Point.Line(root.point0, root.point1)

	# translate to origin
	new_line.translate(-root.point0.x, -root.point0.y)

	# rotate and scale
	if turn[i-1] == 'R':
		new_line.rotate(1.5708)
	else:
		new_line.rotate(-1.5708)

	# translate back
	new_line.translate(root.point0.x, root.point0.y)

	# translate tail to head of root
	new_line.translate(root.point1.x - root.point0.x, root.point1.y - root.point0.y)

	return new_line

##### i = iterations, l = line_length, c = colour, t = turn
def recursive_draw(root, i, l, c, t):
	# end recursion if base case reached
	if (i == 0):
		return

	# print root
	print 'line', root, c

	# continue with recursion
	recursive_draw(next_line(root,i,t), i-1, l, c, t)

##### i = iterations, l = line_length, c = colour, t = turn
def iterative_draw(root, i, l, c, t):
	count = 0
	pair = 0
	while count < i:
		count = count + 1
		print 'line', root, c
		root = next_line(root,i,t)
		i = i - 1
		
##### i = iterations, l = line_length, c = colours in list, t = turn
def iterative_draw_c(root, i, l, c, t):
	count = 0
	pair = 0
	while count < i:
		if count%100 == 0:
			pair = pair + 1
			if pair == c:
				pair = 0
		count = count + 1
		print 'line', root, colours[pair]
		root = next_line(root,i,t)
		i = i - 1	

		


#### not usable past 8 iterations, python caps at 999 iterations
def recursive_map(map, i):
	if i == 0:
		return map
	else:
		map.append('R')
		offset = len(map)
		for x in reversed(map[:offset-1]):
			if x == 'R':
				map.append('L')
			else:
				map.append('R')
		return recursive_map(map, i-1)
#### usable past 8 iterations
def iterative_map(map, i):
	count = 0
	while count < i:
		count = count + 1
		map.append('R')
		offset = len(map)
		for y in reversed(map[:offset-1]):
			if y == 'R':
				map.append('L')
			else:
				map.append('R')
	return map	

# ********** process the command line arguments
if len(sys.argv) != 4:
	print >> sys.stderr, 'Requires command line input: ' + sys.argv[0] + ' iterations line_length colour'
	sys.exit(1)
try:
	iterations = int(sys.argv[1])
	line_length = float(sys.argv[2])
	colour = str(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Requires command line input: ' + sys.argv[0] + ' iterations(int > 0) line_length(float > 0) colour(String)'
	sys.exit(2)
if iterations < 1 or line_length < 1:
	print >> sys.stderr, 'Requires command line input: ' + sys.argv[0] + ' iterations(int > 0) line_length(float > 0) colour(String)'
	sys.exit(3)
# colour scheme idea
colours = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenRod', 'DarkGray', 'DarkGrey', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DimGrey', 'DodgerBlue', 'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod', 'Gray', 'Grey', 'Green', 'GreenYellow', 'HoneyDew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey', 'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple', 'RebeccaPurple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 'YellowGreen']

fun = False
if colour == 'Fun':
	fun = True

# root: length line_length, in middle of canvas
point0 = Line_Point.Point(0.0,-100.0)
point1 = Line_Point.Point(0.0,-100.0 + line_length)
root = Line_Point.Line(point0, point1)
map = ['R']
new_map = iterative_map(map, iterations)
its = len(new_map)
cs = len(colours)


if fun:
	iterative_draw_c(root,its,line_length,cs,new_map)
else:
	iterative_draw(root,its,line_length,colour,new_map)
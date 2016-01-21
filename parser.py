from svg2plt import SVG2PLT

InFileName = 'owl.svg'
OutFileName = 'owl.hpgl'

svg2plt = SVG2PLT()
svg2plt.parse_file(InFileName)

OutFile = open(OutFileName, 'w')
OutFile.write(svg2plt.plt)
OutFile.close() 

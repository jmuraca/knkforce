from svg2plt import SVG2PLT

InFileName = 'owl.svg'
OutFileName = 'owl.hpql'

svg2plt = SVG2PLT()
svg2plt.parse_file(InFileName)

OutFile = open(OutFileName, 'w')
OutFile.write(svg2plt.plt)
OutFile.close() 

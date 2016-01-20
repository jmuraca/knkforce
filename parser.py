from svg2plt import SVG2PLT

svg2plt = SVG2PLT()
svg2plt.start()

InFileName = 'owl.svg'
OutFileName = 'owl.hpql'

OutFile = open(OutFileName, 'w')


svg2plt.parse_file(InFileName)

svg2plt.end()

OutFile.write(svg2plt.plt)
OutFile.close() 

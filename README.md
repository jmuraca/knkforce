# KNK Force
## An open python software interface
This software hopes to provide an open and hackable software interface for anyone to install on to their KNK Force and come up with some really amazing uses!

The KNK Force is a desktop CNC cutter/plotter with a built in Raspberry Pi for the brains and a serial connected motor controller board to interface to the stepper motors. The on board Raspberry Pi connects to your home WiFi network via a USB dongle and acts as a local web server for you to upload files to cut.
The dual head is not simply and up/down driver like a normal cutter but offers an incremental Z-axis motion. It has a rotary bit attachment which allows cutting of plastics or wood material too. The head also has a camera in built (!) which when the drivers get working will allow being able to put in a piece of paper with a shape, capture it on the camera, then automatically cut it.

###### Interface screenshot
![KNK Forcepython hack interface](knk_force_python_hack.png?raw=true "KNK Forcepython hack interface")

###### Backend
When I got my cutter I very quickly cracked it open and tried to customise the code but it was written in Ruby and is encrypted :(
I removed the default SD card and installed my own version of Raspbian on it and wrote a Python driver to convert SVG to the custom PLT instruction format. This offers the basic cutter tools but there is so much more that this could do.

The backend software is written in Python and is used for both the webserver and serial comms. 
- The webserver for this project is [Flask](http://flask.pocoo.org/), as it is super light weight, easy to use, and allows easy file and serial operations
- Serial communications to the motor driver board use [pySerial](https://github.com/pyserial/pyserial) on '/dev/ttyAMA0' using a defined set of commands
- SVG parsing is performed by [svg.path](https://pypi.python.org/pypi/svg.path) (with a bith of extra cleaning up)

###### Frontend
The front web interface uses a standard HTML/CSS/JS
- [Semantic UI](http://semantic-ui.com/) is used for the CSS styles to make the site look slick and provide some mobile/tablet compatiblity.

###### Installation
This has been test on Raspbarian Jessie. Download a fresh Raspbarian image and follow the installation instructions in installation.txt file

###### The future
I have a hardware background and what I would ultimately like to do with this is turn it into a PCB factory! Using the rotary bit I want to be able to export proto boards from Eagle and cut them on this cutter. Replace the rotary with a drill bit and drill the holes. PCB's are so cheap now that that could be not needed. But the real plus for me would be to add a vacuum pump and do some pick and place of parts PLUS use the camera for visual checks! That's hopefully what I'll be able to do with this software. Lots of work but would be awesome!


**Disclaimer**
This project was started by James Muraca to run on a KNK Force and the source is available at [GitHub](https://github.com/jmuraca/knkforce/). I've learnt a lot from this project. This is my first go at coding in Python, using Linux in an embedded way, and my first open sourced project. 

All of the code is on Github and hopefully the community can use this as a base and build upon it too. This software is open for anyone to hack so please help to contribute new features and make it even more awesome!

The Klic-N-Kut name and logo, and the KNK Force name and logo, are trademarks of [AccuGraphic Sales, Inc.](http://knkusa.com/)

KNK Force is distributed in Australia and New Zealand by [Skat Katz](http://www.skatkatz.com.au)

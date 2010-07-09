setAutoWaitTimeout(0.5)

click("1278635612647.png")
myReg =  selectRegion("Select Check area")
#wait("1278645692467.png",3)
while myReg.exists(Pattern("1278645598685.png").similar(0.80)):
	myReg.click(Pattern("1278645598685.png").similar(0.80))
	sleep(2)
popup("All pass is click!")
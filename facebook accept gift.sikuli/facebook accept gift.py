setAutoWaitTimeout(0.5)

def doclick(check_pic,exit_pic):
	if exists(check_pic):
		click(exit_pic)
		return True
	else:
		return False

do_list = []
do_list.append (["1278608259549.png","1278608339373.png"])
do_list.append (["1278635179596.png","1278635208662.png"])
do_list.append (["1278637268476.png","1278637289122.png"])
do_list.append (["1278637396726.png","1278637412358.png"])
do_list.append (["1278637877266.png","1278637901192.png"])
do_list.append (["1278706850127.png","1278706880034.png"])

# Main
click("1278635612647.png")
wait("1278608682415.png",5)
while exists("1278608126706.png"):
	click("1278608126706.png")
	waitVanish("1278608682415.png")
	for d in do_list:
		if doclick(d[0],d[1]):
			break
	sleep(2)
popup("All Accept is click!")
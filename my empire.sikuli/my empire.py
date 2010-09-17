setThrowException(True)
#setShowActions(True)

switchApp("Google 瀏覽器")
click("1276335840892.png")
doubleClick(Pattern("1276333215717.png").similar(0.45))
hover("1276336170212.png")
wait("1276335598837.png",5)
click("1276335598837.png")
wait("1276332854574.png")
click(Pattern("1276332854574.png").targetOffset(-16,-47))



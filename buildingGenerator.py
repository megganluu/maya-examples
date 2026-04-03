import maya.cmds as mc
if mc.window(myWindow, exists=True):
        mc.deleteUI(myWindow)

myWindow = mc.window(title="Building Generator", w=300, h=200)
mc.columnLayout(adjustableColumn=True)

mc.button(label='Create building!', h =50, c='makeBuilding(10)')
mc.separator(h=10, style="double")
mc.showWindow(myWindow)

def makeBuilding(myHeight):
    myBuilding = mc.polyCube(h=myHeight)
    mc.move(0, float(myHeight/2), 0)
    mc.polyExtrudeFacet(myBuilding[0] + ".f[1]", ltz=0.5, ls=(0.1, 0.1, 0))
    mc.select(clear=True)


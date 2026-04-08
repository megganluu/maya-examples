import maya.cmds as mc

rWindow = mc.window("radWindow", t="Slider", w=300, h=300)
mc.columnLayout(adj=True)

mc.text("Choose the radius")
radiusSlider = mc.intSliderGrp(l = "Radius", min=0, max=10, field=True)
mc.button(label="Create a sphere", command="makeSphere()")
mc.showWindow(rWindow)

def makeSphere():
      rad = mc.intSliderGrp(radiusSlider, q=True, v=True)
      sphere = mc.polySphere(r=rad, n="ball")
      mc.move(0, rad, 0, sphere)
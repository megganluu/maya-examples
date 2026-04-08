# Ball Pit Generation
import maya.cmds as mc
import random

win = mc.window("myWindow", t="Ball Pit Generator", w=300, h=100)
mc.columnLayout(adj=True)

# User Input
mc.text("Create a static 3D ball pit")
sizeSlider = mc.intSliderGrp(l="Ball Size", min=1, max=5, f=True)
tankSlider = mc.intSliderGrp(l="Pit Size", min = 2, max=10, f=True)
ballSlider = mc.intSliderGrp(l="Num Balls", min = 10, max=20, f=True)

mc.button(label="Generate Ball Pit", command="makeBallPit()")

mc.showWindow(win)

def makeBall():
    rad = mc.intSliderGrp(sizeSlider, q=True, v=True) / 5
    ball = mc.polySphere(r=rad, n="Ball#")
    return ball
    
def makeBallPit():
    side = mc.intSliderGrp(tankSlider, q=True, v=True)
    N = mc.intSliderGrp(ballSlider, q=True, v=True)
    rad = mc.intSliderGrp(sizeSlider, q=True, v=True)
    
    # Arrange balls
    for i in range(N):
        name = "Ball" + str(i + 1)
        b = makeBall()
        # translations
        xT = random.uniform(-side/2, side/2)
        yT = min(random.uniform(0, side) + rad / 5, side - rad)
        zT = random.uniform(-side/2, side/2)
        mc.move(xT, yT, zT, b)
        
    pit = mc.polyCube(w=side, h=side, d=side, n="Pit")
    mc.move(0, side/2, 0, pit)
    
    color = mc.shadingNode("surfaceShader", asShader=True, name="blueShader")
    mc.setAttr(color + '.outColor', 0, 0, 1, type="double3")
    mc.setAttr(color + '.outTransparency', 0.7, 0.7, 0.7, type="double3")
    
    sg = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name="blueSG")
    mc.connectAttr(color + '.outColor', sg + '.surfaceShader', f=True)
    
    top = mc.shadingNode('surfaceShader', asShader=True, name='topInvisibleShader')
    mc.setAttr(top + '.outColor', 0, 0, 1, type='double3')
    mc.setAttr(top + '.outTransparency', 1, 1, 1, type='double3')
    
    sgT = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='topInvisibleSG')
    mc.connectAttr(top + '.outColor', sgT + '.surfaceShader', f=True)
    
    for obj in pit:
        faces = cmds.ls(obj + ".f[*]", fl=True)
        topFace = None
        topY = -999999
    
        # Find the top face
        for f in faces:
            pos = mc.xform(f, q=True, ws=True, t=True)
            y = pos[1]
            if y > topY:
                topY = y
                topFace = f
    
        mc.sets(faces, edit=True, forceElement=sg)
    
        if topFace:
            mc.sets(topFace, edit=True, forceElement=sgT)
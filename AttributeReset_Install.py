import maya.cmds as cmds
import maya.mel as mel

labelName = 'Default'
annot = 'ResetAttribute'
imagePath = 'commandButton.png'
imageLabel = 'Default'
sourceScript = 'python'
btnName = 'Default_btn'

def myTool():
    cmds.warning("My Tool is running!")

def createShelfButton():
    shelf = mel.eval('$gShelfTopLevel=$gShelfTopLevel')
    currentShelf = cmds.tabLayout(shelf, q=True, selectTab=True)
    if cmds.shelfButton(btnName, exists=True):
        cmds.warning("{} already installed.".format(label))
        return
    
    command = '''import maya.cmds as cmds
import maya.mel as mel

def attr0():
    sels = cmds.ls(sl=True)
    if not sels:
        cmds.warning("sohai select smtg la")
        return
    channelBox = mel.eval('global string $gChannelBoxName; $temp=$gChannelBoxName;') #Fetch maya's main channelbox
    attrBox = cmds.channelBox(channelBox,q=True,sma=True)
    noChange = True
    for sel in sels:
        attrs = attrBox or cmds.listAttr(sel, k=True, u=True) or []
        for attr in attrs:
            plug = "{}.{}".format(sel,attr)
            if not cmds.objExists(plug):
                continue
            if cmds.getAttr(plug,lock=True):
                continue
            try:  
                defaultVal = cmds.attributeQuery(attr,node=sel,listDefault=True)
                if not defaultVal:
                    continue
                defaultVal = defaultVal[0]
                attrType = cmds.getAttr(plug,type=True)
                currentVal = cmds.getAttr(plug)
                # VECTOR / COMPOUND (translate, rotate, scale, float3, double3)
                if attrType in ("double3", "float3"):
                    cur = currentVal[0]
                    if isinstance(defaultVal,(list,tuple)):
                        defVal = tuple(defaultVal)
                    else:
                        defVal = (defaultVal, defaultVal, defaultVal)
                    if cur != defVal:
                        cmds.setAttr(plug, *defVal)
                        noChange = False
                # STRING
                elif attrType == "string":
                    if currentVal != defaultVal:
                        cmds.setAttr(plug, defaultVal, type="string")
                        noChange = False
                # ENUM
                elif attrType == "enum":
                    if currentVal != int(defaultVal):
                        cmds.setAttr(plug, int(defaultVal))
                        noChange = False
                # NUMERIC (float, double, int, etc.)
                else:
                    if currentVal != defaultVal:
                        cmds.setAttr(plug, defaultVal)
                        noChange = False
            except Exception as e:
                cmds.warning("Skipped {} : {}".format(plug, e))
    if noChange:
        cmds.warning("Its already default value bruh")
attr0()
'''

    cmds.shelfButton(parent=currentShelf,
    				 label=labelName,
    				 annotation=annot,
    				 image=imagePath,
    				 imageOverlayLabel=imageLabel,
    				 overlayLabelColor=(1, 1, 1),
    				 overlayLabelBackColor=(0.2, 0.5, 0.9, 0.85),
    				 command=command,
    				 sourceType=sourceScript
					)

def onMayaDroppedPythonFile(*args):
    createShelfButton()
    cmds.inViewMessage(amg='<hl>Default</hl> installed successfully!',pos='topCenter',fade=True)
    cmds.warning("{} installation complete.".format(labelName))
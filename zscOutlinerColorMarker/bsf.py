#!/usr/bin/python
# -*- coding: UTF-8 -*-

import maya.cmds as cmds

def func_unset(*ic):
	ic = {
		'(\'q\',)':'question',
		'(\'i\',)':'information',
		'(\'w\',)':'warning',
		'(\'c\',)':'critical'
	}.get(str(ic),'information')
	cmds.confirmDialog(m='Comming Soon..',icon=ic[0])

def get_outliner_color():
	ret = cmds.ls('*.outlinerColor',l=1,r=1)
	return ret

def set_no_color():
	sels = cmds.ls(sl=1)
	for o in sels:
		cmds.setAttr('%s.useOutlinerColor'%o,0)

def ck_exist_win(*win):
	if cmds.window(win[0],ex=1):
		cmds.deleteUI(win[0])



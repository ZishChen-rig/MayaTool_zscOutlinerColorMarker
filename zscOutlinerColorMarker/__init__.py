#!/usr/bin/python
# -*- coding: UTF-8 -*-

import maya.cmds as cmds

def info():
	ret = cmds.confirmDialog(
		t='Tool Information',
		icn='information',
		m='''
		<br>
			<table border=".1" width="500">
				<tr>
					<td><p align="right"><font size=\'5\' color=\'#0B1013\'>tool_name : </font></p></td>
					<td><font size=\'5\' color=\'#0C4842\'>Outliner_Color_Marker</font></td>
				</tr>
				<tr>
					<td><p align="right"><font size=\'5\' color=\'#0B1013\'>tool version : </font></p></td>
					<td><font size=\'5\' color=\'#0C4842\'>0.0.1</font></td>
				</tr>
				<tr>
					<td><p align="right"><font size=\'5\' color=\'#0B1013\'>author : </font></p></td>
					<td><font size=\'5\' color=\'#0C4842\'>Zish Chen</font></td>
				</tr>
				<tr>
					<td><p align="right"><font size=\'5\' color=\'#0B1013\'>minimum_version : </font></p></td>
					<td><font size=\'5\' color=\'#0C4842\'>maya 2016</font></td>
				</tr>
				<tr>
					<td><p align="right"><font size=\'5\' color=\'#0B1013\'>call_ui_script : </font></p></td>
					<td>
						<font size=\'5\' color=\'#0C4842\'>
							import zscOutlinerColorMarker.uim<br>
							reload(zscOutlinerColorMarker.uim)<br>
							zscOutlinerColorMarker.uim.ocm()
						</font>
					</td>
				</tr>
			</table>
		''',
		b=['Home page','Close'], bgc=[.8,.85,.74],
		cb='Close', ds='Close', db='Close'
	)
	if ret == 'Home page':
		try:import webbrowser
		except:pass
		webbrowser.open('https://zishchenrig.blogspot.com/')
	return






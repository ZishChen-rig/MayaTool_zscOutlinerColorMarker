#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import maya.cmds as cmds

class cls_stl:
	
	def ui_tt(self,*txt,**flg):
		cw = flg.get('cw',(1,1))
		fc = flg.get('fc','999')
		bgc = flg.get('bgc',[0.109, 0.109, 0.109])
		lyt = cmds.rowColumnLayout(
			p=self.m_lyt_col, nc=len(cw), cs=[(1,5)], bgc=bgc,
			cw=[(i+1,((self.win_wh[0]-10)/sum(cw))*cw[i]) for i in range(len(cw))]
		)
		cmds.text(
			l='<font size=\'3\' color=\'#%s\'>- %s</font>'%(fc,txt[0]),
			al='left',en=0
		)
		cmds.separator(st='in',h=15)
		return lyt
	
	def ui_lyt_prd(self,*cw):
		if len(cw) == 1:
			lyt = cmds.rowColumnLayout(
				p=self.m_lyt_col, nc=len(cw),
				cw=[(i+1,self.win_wh[0]/sum(cw)*cw[i]-15.0) for i in range(len(cw))],
				cs=[(i+1,5) for i in range(len(cw)+1)]
			)
		else:
			lyt = cmds.rowColumnLayout(
				p=self.m_lyt_col, nc=len(cw),
				cw=[(i+1,self.win_wh[0]/sum(cw)*cw[i]-10.0/len(cw)) for i in range(len(cw))],
				co=[(i+1,'left',5) for i in range(len(cw)-1)]
			)
		return lyt
	
	def ui_fp(self,*m):
		path = cmds.fileDialog2(
			fm=m[0], dir=os.path.dirname(__file__),
			ff='OutlinerMarkColor Files (*.ocm);;Text Files (*.txt)'
		)
		return path
	
	def c_hex(self):
		hex = cmds.promptDialog(
			t='Hex', m='Input hex',
			b=['Get','Set','Cancel'],
			db='Cancel', cb='Cancel', ds='Cancel',
			tx='#ffffff'
		)
		if hex == 'Cancel':return
		xc = cmds.promptDialog(q=1,tx=1).replace('#','')
		if len(xc) == 3:
			xc = ''.join([c*2 for c in xc])
		xc = [round(float(int(xc[i*2:i*2+2],16))/float(256),self.v_rnd) for i in range(len(xc)/2)]
		cmds.colorSliderGrp(self.xc_ui_sld,e=1,rgb=xc)
		if hex == 'Set':
			self.xc_btn_set()





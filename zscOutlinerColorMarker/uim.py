#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
from maya import cmds
from . import (
	bsf as biFc,
	ust as siFc
)

class ocm(siFc.cls_stl):
	
	def __init__(self):
		self.win_n = 'zscOutlinerColorMarker'
		self.win_t = 'OutlinerColorMarker'
		self.win_wh = (200,280)
		self.v_rnd = 3
		self.xc_list = []
		self._xc_sl = None
		self.gui()
	
	def gui(self):
		biFc.ck_exist_win(self.win_n)
		cmds.window(self.win_n)
		self.m_lyt_col = cmds.rowColumnLayout(nr=10,rs=[(i+1,2) for i in range(10)],bgc=[0.215, 0.234, 0.219])
		self.ui_tt('Set Color',cw=(3,5))
		self.ui_lyt_prd(1,1)
		self.xc_ui_sld = cmds.colorSliderGrp(rgb=(.375,.375,.375),cw=[(1,(self.win_wh[0]-10)/2),(2,1)])
		cmds.button(l='HEX',h=15,c=lambda *a:self.c_hex())
		self.ui_tt('Color Records',cw=(6,8))
		self.xc_g_lyt_scl = cmds.scrollLayout(p=self.m_lyt_col,w=self.win_wh[0]-5,h=self.win_wh[0]/3,bgc=[0.047, 0.047, 0.047])
		self.xc_g_lyt_rc = cmds.rowColumnLayout(p=self.xc_g_lyt_scl,nc=10)
		self.ui_lyt_prd(1,1,1,1,1)
		cmds.iconTextButton(st='iconOnly',i='setEdAddCmd.png',c=lambda *a:self.xc_btn_add())
		cmds.iconTextButton(st='iconOnly',i='setEdRemoveCmd.png',c=lambda *a:self.xc_btn_rmv())
		cmds.iconTextButton(st='iconOnly',i='removeRenderable.png',c=lambda *a:self.xc_btn_clear())
		cmds.iconTextButton(st='iconOnly',i='fileSave.png',c=lambda *a:self.xc_fp_save())
		cmds.iconTextButton(st='iconOnly',i='fileOpen.png',c=lambda *a:self.xc_fp_load())
		self.ui_lyt_prd(2,3)
		cmds.text(l='<font size=\'3\' color=\'#ccc\'>Click Mode :</font>')
		self.xc_omu_op = cmds.optionMenu(h=30)
		for i in ['Get Color','Set Color','Select Dyed Objects']:
			cmds.menuItem(l=i)
		self.ui_tt('Operational',cw=(3,5))
		self.ui_lyt_prd(1)
		cmds.button(l='Scan Outliner Colors to Record',h=30,c=lambda *a:self.xc_btn_scan(),bgc=[0.395, 0.402, 0.395])
		self.ui_lyt_prd(1,1)
		cmds.button(l='Marking Color',h=30,c=lambda *a:self.xc_btn_set(),bgc=[0.395, 0.402, 0.395])
		cmds.button(l='Remove Color',h=30,c=lambda *a:biFc.set_no_color(),bgc=[0.395, 0.402, 0.395])
		cmds.showWindow(self.win_n)
		cmds.window(self.win_n,e=1,t=self.win_t,wh=self.win_wh,s=0)
		df_fp_ocm = os.path.join(os.path.dirname(__file__),'default.ocm')
		if os.path.exists(df_fp_ocm):
			self.xc_fp_load(df_fp_ocm)
	
	def xc_to_rgb(self):
		for i in range(len(self.xc_list)):
			self.xc_list[i] = [float(c) for c in self.xc_list[i].split(',')]
	
	def xc_to_str(self):
		rcs = re.compile(r'[[](.*?)[]]', re.S)
		for i in range(len(self.xc_list)):
			self.xc_list[i] = [round(c,self.v_rnd) for c in self.xc_list[i]]
		self.xc_list = [re.findall(rcs,str(c).replace(' ',''))[0] for c in self.xc_list]
		self.xc_list = list(set(self.xc_list))
	
	def xc_reset(self):
		self.xc_to_str()
		self.xc_to_rgb()
	
	def xc_btn_set(self):
		self.xc_btn_add()
		xc = cmds.colorSliderGrp(self.xc_ui_sld,q=1,rgb=1)
		for o in cmds.ls(sl=1):
			cmds.setAttr('%s.useOutlinerColor'%o,1)
			cmds.setAttr('%s.outlinerColor'%o,xc[0],xc[1],xc[2])
	
	def xc_fp_save(self):
		path = self.ui_fp(0)
		if not path:return
		self.xc_to_str()
		with open(path[0],'w') as f:
			for c in self.xc_list:
				f.writelines('%s@\r\n'%c)
	
	def xc_fp_load(self,*path):
		if not path:
			path = self.ui_fp(1)
		if not path:return
		self.xc_list = []
		with open(path[0],'r') as f:
			for xc in f.readlines():
				if '@' not in xc:continue
				xc = xc.replace(' ','').split('@')[0]
				self.xc_list += [xc]
		self.xc_to_rgb()
		self.xc_btn_kill()
		self.xc_btn_build()
	
	def xc_btn_rec(self,*xc):
		xc = xc[0]
		def xc_btn_fc(btn):
			md = cmds.optionMenu(self.xc_omu_op,q=1,sl=1)
			self._xc_sl = btn
			if md == 1:
				cmds.colorSliderGrp(self.xc_ui_sld,e=1,rgb=xc)
			elif md == 2:
				for o in cmds.ls(sl=1):
					cmds.setAttr('%s.useOutlinerColor'%o,1)
					cmds.setAttr('%s.outlinerColor'%o,xc[0],xc[1],xc[2])
			elif md == 3:
				sel = []
				for oat in biFc.get_outliner_color():
					obj = oat.split('.')[0]
					val = [round(c,self.v_rnd) for c in cmds.getAttr(oat)[0]]
					if not cmds.getAttr('%s.useOutlinerColor'%obj):continue
					if val != xc:continue
					sel += [obj]
				cmds.select(sel,r=1)
		bXc = cmds.button(
			p=self.xc_g_lyt_rc, l=' ', bgc=xc,
			w=(self.win_wh[0]-20)/10,h=(self.win_wh[0]-20)/10
		)
		cmds.button(bXc,e=1,c=lambda *a:xc_btn_fc(bXc))
		return bXc
	
	def xc_btn_add(self):
		xc = cmds.colorSliderGrp(self.xc_ui_sld,q=1,rgb=1)
		xc = [round(c,self.v_rnd) for c in xc]
		if xc not in self.xc_list:
			self.xc_list += [xc]
		self.xc_btn_kill()
		self.xc_btn_build()
	
	def xc_btn_rmv(self):
		xc = cmds.button(self._xc_sl,q=1,bgc=1)
		xc = [round(c,self.v_rnd) for c in xc]
		self.xc_list.remove(xc)
		self.xc_btn_kill()
		self.xc_btn_build()
		self._xc_sl = None
	
	def xc_btn_clear(self):
		self.xc_btn_kill()
		self.xc_list = []
		self.xc_btn_build()
	
	def xc_btn_build(self):
		self.xc_reset()
		for xc in self.xc_list:
			self.xc_btn_rec(xc)
	
	def xc_btn_kill(self):
		cmds.deleteUI(self.xc_g_lyt_rc)
		self.xc_g_lyt_rc = cmds.rowColumnLayout(
			p=self.xc_g_lyt_scl, nc=10,
			bgc=[0.031, 0.031, 0.031]
		)
	
	def xc_btn_scan(self):
		self.xc_btn_kill()
		self.xc_list = []
		for oat in biFc.get_outliner_color():
			if not cmds.getAttr('%s.useOutlinerColor'%oat.split('.')[0]):continue
			xc = cmds.getAttr(oat)[0]
			self.xc_list += [xc]
		self.xc_btn_build()

if __name__ == '__main__':
	ocm()







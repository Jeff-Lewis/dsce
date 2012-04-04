# This file is part of the DomainSharedContactsEditor (DSCE) application.
#
# DSCE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DSCE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DSCE.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (c) 2012 Klaus Melcher (melcher.kla@gmail.com)

import wx
import xrcl

import logging as log
import sys 

import domaindata

import observer
from observer import pmsg 

# list control configuration
COLIDX_NAME = 0
COLIDX_TYPE = 1
LABEL_NAME = "Group Name"
LABEL_TYPE = "Type"
TYPE_TXT_PRI = "Private"
TYPE_TXT_SYS = "System"
TYPE_ARR = [TYPE_TXT_PRI, TYPE_TXT_SYS]

LABEL_ADD = "Add"
LABEL_UPD = "Update"
LABEL_DEL = "Delete"

class GroupEditDialog(wx.Dialog):

    def __init__(self, parent, ID=-1, title="Manage Groups"):

        wx.Dialog.__init__(self, parent, ID, title, 
                           style=wx.DEFAULT_DIALOG_STYLE
                                 #| wx.RESIZE_BORDER
                           )
        self.idx = -1
        self.isSystemGroup = False
        self.haveChanges=False

        # sg = system groups, pg = private groups
        self.sg, self.pg = domaindata.get_group_names()

        self.panel = xrcl.loadPanel(self, "groupeditor.xrc", "groupeditor")
        self.glc = xrcl.getControl(self.panel, "grplstctrl")

        self.gnc = xrcl.getControl(self.panel, "grpname")

        self.gtc = xrcl.getControl(self.panel, "typechoice")

        self.uab = xrcl.getControl(self.panel, "upaddbutton")
        self.uab.SetLabel(LABEL_ADD)
        self.deb = xrcl.getControl(self.panel, "delbutton")
        self.deb.SetLabel(LABEL_DEL)
        

        self.populateForm()
        
        space = 5
        self.topSizer = wx.BoxSizer(wx.VERTICAL)
        self.topSizer.Add(self.panel, 1, wx.EXPAND, space)
        self.SetSizer(self.topSizer)
        self.topSizer.Fit(self)

        self.binEvents()

        self.ShowModal()

    def populateForm(self):
        """Fills tha form with existing data if any."""

        self.glc.InsertColumn(COLIDX_NAME, LABEL_NAME)
        self.glc.InsertColumn(COLIDX_TYPE, LABEL_TYPE)
        for g in self.sg:
            self.appendGroup(g, TYPE_TXT_SYS)
        for g in self.pg:
            self.appendGroup(g, TYPE_TXT_PRI)

        self.gtc.SetItems(TYPE_ARR)
        self.setFormType()

    def binEvents(self):
        xrcl.getControl(self.panel, "wxID_OK").Bind(wx.EVT_BUTTON, self.onOk)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected, self.glc)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.onItemDeselected, self.glc)
        self.Bind(wx.EVT_BUTTON, self.onAddOrUpdate, self.uab)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deb)

    def setFormType(self, t=None):
        if t:
            try:
                self.gtc.SetSelection(TYPE_ARR.index(t))
            except:
                self.gtc.SetSelection(0)
        else:
            self.gtc.SetSelection(0)

    def onItemSelected(self, event):
        self.idx = event.GetIndex()
        self.gnc.SetValue(self.glc.GetItem(self.idx, COLIDX_NAME).GetText())
        self.setFormType(self.glc.GetItem(self.idx, COLIDX_TYPE).GetText())
        self._setDelButton()
        self._setUAButton()

    def clearForm(self):
        self.idx = -1
        self.gnc.SetValue("")
        self.setFormType()
        self._setDelButton()
        self._setUAButton()

    def onDelete(self, event):
        if self.idx >= 0:
            self.glc.DeleteItem(self.idx)
            self.clearForm()


    def onAddOrUpdate(self, event):
        name = self.gnc.GetValue().strip()
        gtype= TYPE_ARR[self.gtc.GetSelection()]

        if len(name) == 0: return

        if self.idx < 0:
            self.appendGroup( name, gtype)
            self.clearForm()
        else:
            self.updateGroup( self.idx, name, gtype)


    def onItemDeselected(self, event):
        self.clearForm()

    def _setDelButton(self):
        if self.idx < 0 or TYPE_ARR[self.gtc.GetSelection()] == TYPE_TXT_SYS:
            self.deb.Disable()
        else:
            self.deb.Enable()

    def _setUAButton(self):
        if self.idx < 0:
            self.uab.SetLabel(LABEL_ADD)
        else:
            self.uab.SetLabel(LABEL_UPD)


    def saveChanges(self):
        """Saves if anything (except primary or type) has been set."""
        pass

    def appendGroup(self, name, gtype=TYPE_TXT_PRI):
        idx = self.glc.InsertStringItem(sys.maxint, name)
        self.glc.SetStringItem(idx, COLIDX_TYPE, gtype)
        self.haveChanges = True

    def updateGroup(self, idx, name, gtype):
        self.glc.SetStringItem(idx, COLIDX_NAME, name)
        self.glc.SetStringItem(idx, COLIDX_TYPE, gtype)
        self.haveChanges = True


    def onOk(self, event):
        log.debug("Save changes in groups")
        self.saveChanges()
        self.Destroy()
        

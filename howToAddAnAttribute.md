<h1>How to add an additional attribute support</h1>

# Summary #

This page describes how to extend the program to support an additional attribute which is already part of the Google contact falvour but not already editable by the DomainSharedContactsEditor.

In this example we are going to add the support for an `organisation` the contact is associated with.

# Index #



# Identify Data and API #

Within `gdata.contacts.data.ContactEntry` the organisation attribute is defined as follows:
```
organization = gdata.data.Organization
```

Organizations attributes are described [here](http://code.google.com/apis/gdata/docs/2.0/elements.html#gdOrganization)

So we'll have to deal with the following structure:

```
start = organization

organization =
   element gd:organization {
      attribute label { xs:string }?,
      attribute rel { xs:string }?,
      attribute primary { xs:boolean }?,
      ( orgDepartment? &
      orgJobDescription? &
      orgName? &
      orgSymbol? &
      orgTitle? &
      where? )
   }
```

Which resluts e.g. in

```
<gd:organization rel="http://schemas.google.com/g/2005#work" label="Work" primary="true"/>
  <gd:orgName>Google, Inc.</gd:orgName>
  <gd:orgTitle>Tech Writer</gd:orgTitle>
  <gd:orgJobDescription>Writes documentation</gd:orgJobDescription>
  <gd:orgDepartment>Software Development</gd:orgDepartment>
  <gd:orgSymbol>GOOG</gd:orgSymbol>
</gd:organization>
```

This means we'll have besides simple registering it within the applicaiton also provide an aditional editor and renderer for this attribute.

# Register it within the program. #
We add the organization line to the `domaindata.metadata.py` file as follows:

```
# Use 'c' instead of DomainContact and self, where it has to be implemented by the 
# class that uses this information (see ContactDataTable as an example)
# [ (attributeName, attributeLabel, getterMethod, setterMethod, editable, visible) ]
_META_DATA_=[ ( "uid", "UID", "getUid()", None, False, False),
              ( "prefix", "Prefix", "c.getNamePrefix()", "c.setNamePrefix(value)", True, True),
              ( "family_name","Family Name", "c.getFamilyName()", "c.setFamilyName(value)", True, True),
              ( "given_name", "Given Name", "c.getGivenName()", "c.setGivenName(value)", True, True),
              ( "additional_name", "Additional Name", "c.getAdditionalName()", "c.setAdditionalName(value)", True, True),
              ( "suffix", "Suffix", "c.getNameSuffix()", "c.setNameSuffix(value)", True, True),
              ( "full_name", "Full Name", "c.getFullName()", "c.setFullName(value)", True, True),
              ( "email", "Email", "c.getEmail()", "c.setEmails(value)", True, True),
              ( "phone", "Phone", "c.getPhoneNumber()", "c.setPhoneNumber(value)", True, True),
              ( "postal_address", "Address", "c.getPostalAddress()", "c.setPostalAddress(value)", True, True),
              ( "organization", "Organization", "c.getOrganization()", "c.setOrganization(value)", True, True),
              ( "action", "Action", "c.getAction()", "c.setActionUpdate()", False, False)
            ]
              
IDX_ATTRIBUTE   = 0
IDX_LABEL       = 1
IDX_GETTER      = 2
IDX_SETTER      = 3
IDX_EDITABLE    = 4
IDX_VISIBLE     = 5
```

Furhter implement the corrsponding getter and setter methods also within the DomainContact class. Just to get it running add the following:
```
    def getOrganization(self):
        return self.entry.organization

    def setOrganization(self, org):
        """@param: org = gdata.data.Organization"""
        self.entry.organization = org
```

If you run this it helps you to identify if everithing is working so far and what on organization data you already have in your environment.

# Implement the editor and renderer #

If the renderer is `gui.orgrenderer.OrgCellRenderer` it has to be integrated as follows to the `gridview.py`:

```
...
from orgrenderer import OrgCellRenderer
...
    def setRenderer(self):
        ...
        attr = wx.grid.GridCellAttr()
        attr.SetRenderer(OrgCellRenderer())
        self.SetColAttr(metadata.get_col_idx("organization"), attr)
...

```


# Integrate the editor and renderer into the program #

Let us asume the editor is `gui.orgeditor.OrgEditDialog`. This means you have to add it as follows to the `gridview.py`:

```
...
from orgeditor import OrgEditDialog
...
    def gridEditorRequest(self, evt):
        """Used when others than PyGridCellEditors have to be used.
        """
        c = evt.GetCol()
        if c == metadata.get_col_idx("email"):
            EmailEditDialog(self, -1, self.table, evt.GetRow(), c)
            evt.Veto()
...
        elif c == metadata.get_col_idx("organization"):
            OrgEditDialog(self, -1, self.table, evt.GetRow(), c)
            evt.Veto()
        evt.Skip()

```

# Related links #
  * [Documentation Index](http://www.dsce.org/documentation)
  * [Specifications](Specifications.md)
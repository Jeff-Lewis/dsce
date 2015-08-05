<h1> Technical Specification - Delete one or more contacts</h1>

# Summary #

This page contains the technical specification/implementation of deleting a contact as described on the [Delete Contacts page](http://www.dsce.org/delete-contacts).

# Index #



# Initialisation and deleting a contact #

## Initialisation ##

When creating the tool bar the following relevant messages are registered at the `observer`:
```

class MainFrame(wx.Frame):
...
    def registerMessages(self):
        pmsg.register("DEL_CONTACT") 
...
        pmsg.register("PUB_CONTACT")
```

The message `CONTACT_DELETED` is already registered as part of the initialisation of the `observer-module`.

Further the **DEL** button in the tool bar is bind as follows:
```
 def binEvents(self):
     # toolbar events
...
     self.tb.Bind(wx.EVT_TOOL, self.publishEvent, id=self.DEL_ID)
     self.tb.Bind(wx.EVT_TOOL, self.publishEvent, id=self.PUB_ID)
...

 def publishEvent(self, event):
     """Depending on the id the event with the appropriate message
     will be published.
     """
...
        elif event.GetId() == self.DEL_ID:
            observer.send_message(pmsg.DEL_CONTACT, data=self.grid.getActiveRows())
...
     elif event.GetId() == self.PUB_ID:
         observer.send_message(pmsg.PUB_CONTACT, event)
...
```

Next the {{controller}}} subscribes to the `DEL_CONTACT` event as follows
```
    observer.subscribe(self.delContact, pmsg.DEL_CONTACT)
    observer.subscribe(self.addContact, pmsg.PUB_CONTACT)
```
and the `gridview` subscribes toe the `CONTACT_DELETED` event with
```
     observer.subscribe(self.forceRefresh, pmsg.CONTACT_DELETED) # because of label changes
```

The Resulting picture is the same as descibed in the [technical specification of adding contacts](addContactTs.md). The only difference is that `ADD` is replaced by `DEL` and `ADDED` by `DELETED`.

## Deleting a contact ##

When deleting a contact change of the label name is implemented the same way as for adding or updating a contact.

When the changes has to be published/uploaded to Google the following code in `domaindata.__init__.py` gets executed:

```
def publish_changes():
    """Publish changes made to the contact
    """
...
        elif action == ACTION.DELETE:
            if c.isEmpty():
                logging.warning("Do not publish the deletion of an empty contact %d" % c.getUid())
            else:
                logging.debug("Delete contact %s" % c.getFamilyName())
                _domainContactsClient.deleteContact(c) 
            
            _domainContacts.delete(c)
            _contactDataTable.deleteRow(c)
            del(c)
            logging.debug("deletion finished")
    # rebuild the table index is absolute necessary
    _contactDataTable.rebuildTableIndex()

```

If the contact is not empty it gets deleted at Google `_domainContactsClient.deleteContact(c)`. Then it gets deleted from the local contacts list and the contact table used by the grid. After that the contact itself gets removed from the program context.

At this point all the local stored data are out of sync and therefore it is absolutely necessary to sync all again by calling `_contactDataTable.rebuildTableIndex()`. This method just rebuilds the gridLables and get them aligned with the grid data again.

The deletion at Google is implemented as follows:
```
    def deleteContact(self, contact):
        entry = contact.getEntry()
        self.Delete(entry)
```
As I did not find any useful return value of `self.Delete()` I ignore it.

`domaincontacts.delete()` is just a wrapper for `domaincontacts.pop()`.

The deletion within the grid table is implemented as follows:
```
    def DeleteRows(self, row, numRows=1):
            self.rowLabels.pop(row)
            return True

    def deleteRow(self, c):
            row = self.getRowFromUid(c.getUid())
            self.DeleteRows(row)
            logging.debug("GRIDTABLE_NOTIFY_ROWS_DELETED")
            msg = wx.grid.GridTableMessage(self,
                    wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED,row,1)
            self.grid.ProcessTableMessage(msg) 
```
Mentionable is that the grid itself has to be informed about the deletion of the row. Otherwise it does not work.

# Related links #
  * [Documentation Index](http://www.dsce.org/documentation)
  * [Specifications](Specifications.md)
  * [Adding contacts technical specification](addContactTs.md)
  * [Delete Contacts Functional Description](http://www.dsce.org/delete-contacts).
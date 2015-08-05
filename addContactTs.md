<h1> Technical Specification - Adding one or more contacts</h1>

# Summary #

This page contains the technical specification/implementation of adding a contact described on the [Add Contacts page](http://www.dsce.org/add-contacts).

# Index #



# Initialisation and adding a contact #

## Initialisation ##

When creating the tool bar the following relevant messages are registered at the `observer`:
```

class MainFrame(wx.Frame):
...
    def registerMessages(self):
        pmsg.register("ADD_CONTACT") # request to add a contact
...
        pmsg.register("PUB_CONTACT")
```

The message `CONTACT_ADDED` is already registered as part of the initialisation of the `observer-module`.

Further the **ADD** button in the tool bar is bind as follows:
```
 def binEvents(self):
     # toolbar events
...
     self.tb.Bind(wx.EVT_TOOL, self.publishEvent, id=self.ADD_ID)
     self.tb.Bind(wx.EVT_TOOL, self.publishEvent, id=self.PUB_ID)
...

 def publishEvent(self, event):
     """Depending on the id the event with the appropriate message
     will be published.
     """
     if event.GetId() == self.ADD_ID:
         observer.send_message(pmsg.ADD_CONTACT, event)
...
     elif event.GetId() == self.PUB_ID:
         observer.send_message(pmsg.PUB_CONTACT, event)
...
```

Next the {{controller}}} subscribes to the `ADD_CONTACT` event as follows
```
    observer.subscribe(self.addContact, pmsg.ADD_CONTACT)
    observer.subscribe(self.addContact, pmsg.PUB_CONTACT)
```
and the `gridview` subscribes toe the `CONTACT_ADDED` event with
```
     observer.subscribe(self.appendRow, pmsg.CONTACT_ADDED)
```

The result is that the components are linked together as follows:


<img src='https://wiki.dsce.googlecode.com/hg/images/AddContactsMessage.png' alt='Message overview of adding contacts'>

<i>(The weakness is still the design of the message handling, who registers what, or make it in any case central..?)</i>

<h2>Adding a contact</h2>

When the <b>ADD</b> button in the tool bar is clicked the message <code>ADD_CONTACT</code> is triggered and send to the <code>controller</code> object. After receiving the message the following happens:<br>
<br>
<img src='https://wiki.dsce.googlecode.com/hg/images/Sequence_add_contact.png' alt='Sequence add contact'>

As the sequence shows the <code>controller</code> triggers first the creation of an empty <code>DomainContact</code> object. During the whole process the <code>domaindata</code> module itself acts as an interface to the data and takes care about the correct initialisation.<br>
<br>
After the creation the controller sends the <code>CONTACT_ADDED</code> message to be published by the observer.<br>
<br>
The <code>GridView</code> gets informed and takes all necessary actions to make this change also visible to the user.<br>
<br>
<br>
<h1>Related links</h1>
<ul><li><a href='http://www.dsce.org/documentation'>Documentation Index</a>
</li><li><a href='Specifications.md'>Specifications</a>
</li><li><a href='http://www.dsce.org/add-contacts'>Add Contacts Functional Description</a>.
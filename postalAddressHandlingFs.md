<h1> View and edit postal addresses</h1>

**Status** This specification is under construction.

# Summary #

Postal address viewing and editing within the DomainSharedContactsEditor grid covers all attributes that are described by [Google Data Protocol](http://code.google.com/apis/gdata/docs/2.0/elements.html#gdStructuredPostalAddress).

# Index #



# View Structured Postal Addresses #

# Edit Structured Postal Addresses #

<img src='https://wiki.dsce.googlecode.com/hg/images/pa-editor.png' alt='Postal Address Editor Screenshot'>
<br>

<h2>Behavior</h2>
<ul><li>The list control displays current postal address definitions. One address per line<br>
</li><li>The values of the current selected address in the list controlled are automatically filled in in the form below<br>
</li><li>The button <b><code>&lt;Delete&gt;</code></b> is disabled until something is selected in the list control that can be deleted.<br>
</li><li>The label of the second button should change from <b><code>&lt;Add&gt;</code></b> to <b><code>&lt;Update&gt;</code></b> depending on the what can be done.<br>
</li><li>Changes made in the form are reflected in the list control after <b><code>Add/Update</code></b> has been hit.</li></ul>


<ul><li><b><code>&lt;OK&gt;</code></b> Saves changes made to the selected contact entry.<br>
</li><li><b><code>&lt;Cancel&gt;</code></b> discards all made changes.</li></ul>

<h2>Display Addresses in the Grid</h2>

Within the main screen postal addresses are displayed one address per row. If the structured postal address within the domain contact has a formatted postal address set, their content is displayed. If not the content of street will be used. If this is not set, nothing will be displayed.<br>
<br>
<h2>Help on Attribute</h2>

Beside each attribute a help icon is displayed which, when klicking on it, displays a description of the attribute it refers to.<br>
<br>
<h1>Related links</h1>
<ul><li><a href='Specifications.md'>Specifications</a>
</li><li><a href='postalAddressHandlingTs.md'>Technical specification to handle postal addresses</a>
</li><li><a href='phoneNumberHandling.md'>Phone number handling within DSCE</a></li></ul>

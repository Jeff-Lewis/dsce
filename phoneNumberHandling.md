<h1> DSCE and Phone Numbers</h1>

# Summary #

This page contains notes on how the editing of phone numbers is handled and implemented within the **DomainSharedContactsEditor**.


# Index #




# Data #

## Phone Number Specification ##

Phone numbers are implemented based on the specification [gd:phone](http://code.google.com/apis/gdata/docs/2.0/elements.html#gdPhoneNumber) published by Google.


## Phone Number API ##

Phone numbers are defined within a [Contacts Entry](http://gdata-python-client.googlecode.com/svn/trunk/pydocs/gdata.contacts.data.html#ContactEntry) as follows:

```
phone_number = [<class 'gdata.data.PhoneNumber'>]
```

Within `gdata.data` **PhoneNumber** is defined:

```
class PhoneNumber(atom.core.XmlElement)
        The gd:phoneNumber element.
 
A phone number associated with the containing entity (which is usually
an entity representing a person or a location).
 
    

Method resolution order:
    PhoneNumber
    atom.core.XmlElement
    __builtin__.object

Data and other attributes defined here:

label = 'label'

primary = 'primary'

rel = 'rel'

uri = 'uri'
...

# Data and other attributes inherited from atom.core.XmlElement:

text = None
```


## How to handle rel ##

As with the _structured postal address_ or _email address_ the string **type** or **Type** will be presented to the user instead of **rel**.


The relation between the `rel` value itself and what has to be displayed to the user is as follows:

<table border='1' align='center' cellspacing='0' width='80%'>

<tr>
<th>rel values</th>
<th>String to display</th>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#assistant'>http://schemas.google.com/g/2005#assistant</a>  </td><td> <i>assistant</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#callback'>http://schemas.google.com/g/2005#callback</a>   </td><td> <i>callback</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#car'>http://schemas.google.com/g/2005#car</a>    </td><td> <i>car</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#company_main'>http://schemas.google.com/g/2005#company_main</a>   </td><td> <i>company main</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#fax'>http://schemas.google.com/g/2005#fax</a>    </td><td> <i>fax</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#home'>http://schemas.google.com/g/2005#home</a>   </td><td> <i>home</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#home_fax'>http://schemas.google.com/g/2005#home_fax</a>   </td><td> <i>fax home</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#isdn'>http://schemas.google.com/g/2005#isdn</a>   </td><td> <i>isdn</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#main'>http://schemas.google.com/g/2005#main</a>   </td><td> <i>main</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#mobile'>http://schemas.google.com/g/2005#mobile</a>     </td><td> <i>mobile</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#other'>http://schemas.google.com/g/2005#other</a>  </td><td> <i>other</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#other_fax'>http://schemas.google.com/g/2005#other_fax</a>  </td><td> <i>fax other</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#pager'>http://schemas.google.com/g/2005#pager</a>  </td><td> <i>pager</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#radio'>http://schemas.google.com/g/2005#radio</a>  </td><td> <i>radio</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#telex'>http://schemas.google.com/g/2005#telex</a>  </td><td> <i>telex</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#tty_tdd'>http://schemas.google.com/g/2005#tty_tdd</a>    </td><td> <i>tty/ttd</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#work'>http://schemas.google.com/g/2005#work</a>   </td><td> <i>work</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#work_fax'>http://schemas.google.com/g/2005#work_fax</a>   </td><td> <i>fax work</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#work_mobile'>http://schemas.google.com/g/2005#work_mobile</a>    </td><td> <i>mobile work</i> </td>
</tr>
<tr>
<td> <a href='http://schemas.google.com/g/2005#work_pager'>http://schemas.google.com/g/2005#work_pager</a></td><td> <i>pager work</i> </td>
</tr>

</table>

## Definitions of rel in gdata ##

```
# defined in gdata.data

ASSISTANT_REL = 'http://schemas.google.com/g/2005#assistant'
CALLBACK_REL = 'http://schemas.google.com/g/2005#callback'
CAR_REL = 'http://schemas.google.com/g/2005#car'
COMPANY_MAIN_REL = 'http://schemas.google.com/g/2005#company_main'
FAX_REL = 'http://schemas.google.com/g/2005#fax'
HOME_REL = 'http://schemas.google.com/g/2005#home'
HOME_FAX_REL = 'http://schemas.google.com/g/2005#home_fax'
ISDN_REL = 'http://schemas.google.com/g/2005#isdn'
MAIN_REL = 'http://schemas.google.com/g/2005#main'
MOBILE_REL = 'http://schemas.google.com/g/2005#mobile'
OTHER_REL = 'http://schemas.google.com/g/2005#other'
OTHER_FAX_REL = 'http://schemas.google.com/g/2005#other_fax'
PAGER_REL = 'http://schemas.google.com/g/2005#pager'
RADIO_REL = 'http://schemas.google.com/g/2005#radio'
TELEX_REL = 'http://schemas.google.com/g/2005#telex'
TTL_TDD_REL = 'http://schemas.google.com/g/2005#tty_tdd'
WORK_REL = 'http://schemas.google.com/g/2005#work'
WORK_FAX_REL = 'http://schemas.google.com/g/2005#work_fax'
WORK_MOBILE_REL = 'http://schemas.google.com/g/2005#work_mobile'
WORK_PAGER_REL = 'http://schemas.google.com/g/2005#work_pager'

```


# Related links #

  * [DSCE Homepage](http://www.dsce.org)
  * [Specifications](Specifications.md)
  * [Technical specification to handle postal addresses](postalAddressHandlingTs.md)
  * [Functional specification to handle postal addresses](postalAddressHandlingFs.md)
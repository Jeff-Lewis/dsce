<h1> Techinical Specification - view and edit postal addresses</h1>

# Summary #

This specification describes the technical implementation of the editing (create, update, delete) of the postal address entry within the ` gdata.contacts.data.ContactsEntry ` class.

# Index #



# Data #

## Google data API ##

Within [ContactsEntry](http://gdata-python-client.googlecode.com/svn/trunk/pydocs/gdata.contacts.data.html#ContactEntry) the postal address is implemented as ` postal_address = [<class 'gdata.data.StructuredPostalAddress'>] `.

[StructuredPostalAddress](http://gdata-python-client.googlecode.com/svn/trunk/pydocs/gdata.data.html#StructuredPostalAddress)  _split into components. It allows to store the address
in locale independent format. The fields can be interpreted and used
to generate formatted, locale dependent address. The following elements
reperesent parts of the address: agent, house name, street, P.O. box,
neighborhood, city, subregion, region, postal code, country. The
subregion element is not used for postal addresses, it is provided for
extended uses of addresses only. In order to store postal address in an
unstructured form formatted address field is provided._

It defines:
```
agent = <class 'gdata.data.Agent'>
    The gd:agent element.
     
    The agent who actually receives the mail. Used in work addresses.
    Also for 'in care of' or 'c/o'.

city = <class 'gdata.data.City'>
    The gd:city element.
     
    Can be city, village, town, borough, etc. This is the postal town and
    not necessarily the place of residence or place of business.

country = <class 'gdata.data.Country'>
    The gd:country element.
     
    The name or code of the country.

formatted_address = <class 'gdata.data.FormattedAddress'>
    The gd:formattedAddress element.
     
    The full, unstructured postal address.

house_name = <class 'gdata.data.HouseName'>
    The gd:housename element.
     
    Used in places where houses or buildings have names (and not
    necessarily numbers), eg. "The Pillars".

label = 'label'

mail_class = 'mailClass'

neighborhood = <class 'gdata.data.Neighborhood'>
    The gd:neighborhood element.
     
    This is used to disambiguate a street address when a city contains more
    than one street with the same name, or to specify a small place whose
    mail is routed through a larger postal town. In China it could be a
    county or a minor city.

po_box = <class 'gdata.data.PoBox'>
    The gd:pobox element.
     
    Covers actual P.O. boxes, drawers, locked bags, etc. This is usually
    but not always mutually exclusive with street.

postcode = <class 'gdata.data.Postcode'>
    The gd:postcode element.
     
    Postal code. Usually country-wide, but sometimes specific to the
    city (e.g. "2" in "Dublin 2, Ireland" addresses).

primary = 'primary'

region = <class 'gdata.data.Region'>
    The gd:region element.
     
    A state, province, county (in Ireland), Land (in Germany),
    departement (in France), etc.

rel = 'rel'

street = <class 'gdata.data.Street'>
    The gd:street element.
     
    Can be street, avenue, road, etc. This element also includes the
    house number and room/apartment/flat/floor number.

subregion = <class 'gdata.data.Subregion'>
    The gd:subregion element.
     
    Handles administrative districts such as U.S. or U.K. counties that are
    not used for mail addressing purposes. Subregion is not intended for
    delivery addresses.

usage = 'usage'

```

Structured postal address properties and values are described [on this google page](http://code.google.com/apis/gdata/docs/2.0/elements.html#gdStructuredPostalAddress)

<table width='80%' align='center' border='1'>

<tr>
<blockquote><th align='left'>Details on rel</th>
</tr>
<tr>
<td><b>Value</b></td>
<td><b>Python implementation</b></td>
</tr></blockquote>

<tr>
<blockquote><td><a href='http://schemas.google.com/g/2005#home'>http://schemas.google.com/g/2005#home</a></td>
<td> <code>gdata.data.HOME_REL</code> </td>
</tr></blockquote>

<tr>
<blockquote><td><a href='http://schemas.google.com/g/2005#other'>http://schemas.google.com/g/2005#other</a></td>
<td> <code>gdata.data.OTHER_REL</code> </td>
</tr></blockquote>

<tr>
<blockquote><td><a href='http://schemas.google.com/g/2005#work'>http://schemas.google.com/g/2005#work</a></td>
<td> <code>gdata.data.WORK_REL</code> </td>
</tr></blockquote>

</table>

## Restrictions ##

  * It is forbidden to have both `gd:postalAddress` and `gd:structuredPostalAddress` in one entity.
  * Only one structured address can be specified as primary.
  * The unstructured postal address must be consistent with the structured data.


## domaindata-DomainContact ##

Within the DomainSharedContactsEditor the `PostalAddress` is only accessed by the usage of the provided methods of the `domaindata.DomainContact` class.


## UI Implementation Notes ##

To link the list control and the user interface elements of the form the `domaindata.metadata.AddressMeta.id` is used. This attribute is a two digit unique identifier. All `AddressMeta` objects are initialized in the `metadata` module and stored in an `AddressMetaList` named `AMI` (Address Meta Info).

# Related links #
  * [Specifications](Specifications.md)
  * [Functional specification to handle postal addresses](postalAddressHandlingFs.md)
  * [Phone number handling within DSCE](phoneNumberHandling.md)
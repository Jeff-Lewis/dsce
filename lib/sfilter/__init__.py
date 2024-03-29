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
"""This package provides supporting functions that are used 
in searching.""" 
import logging

import domaindata
from domaindata import spaf
from domaindata import pnf
from domaindata import orgf

# To do the search within each address allows us to 
# return a possible result immideate, when it occures and
# ther is no need to parse possible additional addresses
# of the contact.
def in_address(contact, S):
    pa=contact.getPostalAddress()
    if pa:
        for a in pa:
            if S in spaf.getPA(a).upper():
                return True
    return False 

def in_phone_number(contact, S):
    pn = contact.getPhoneNumber()
    if pn:
        for n in pn:
            if S in pnf.getPhoneNumber(n):
                return True
    return False

def in_organization(contact, S):
    org = contact.getOrganization()
    if org:
        for oe in orgf.getOrgAsStringList(org):
            if S in oe.upper():
                return True 
    return False

def in_group(contact, S):
    grps = contact.getGroups()
    if grps:
        for g in grps:
            if S in domaindata.get_group_name(g.href).upper():
                return True
    return False

def contact_has_string(contact, s):
    """Returns True, if any contact data contains
    the passed string s. This function works NOT case
    sensitive."""
    S=s.upper()
    if (
        (S in contact.getFamilyName().upper()) or
        (S in contact.getGivenName().upper()) or
        (S in contact.getFullName().upper()) or
        (S in contact.getNamePrefix().upper()) or
        (S in contact.getNameSuffix().upper()) or
        (S in contact.getAdditionalName().upper()) or
        (S in str(contact.getEmailAddresses()).upper()) or
        (in_address(contact, S)) or
        (in_phone_number(contact, S)) or
        (in_organization(contact, S)) or
        (in_group(contact, S))
        ): return True
    else:
        return False
    # def getGroups(self):


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
# Copyright (c) 2010 Klaus Melcher (melcher.kla@gmail.com)

"""The package domaindata is responsible to hold/define all necessary data used by dsce.
Further it provides interface methods to access the data itself.

NOTE:
    It is necessary to initialize the package by calling domaindata.init() before
    any other action on the data can be performed.
"""
import gdata.contacts.data
import gdata.contacts.client

import logging

from loginuser import *
from proxysettings import *
from domaincontactsclient import *
from domaincontact import DomainContact
from domaincontact import ACTION
from domaincontacts import DomainContacts
from contactdatatable import *

"""The following objects will be initialized by init()
"""

_domainContactsClient = None
_domainContacts = None
_loginUser = None
_proxySettings = None
_initialized = False # will be set to True at the end of the init() procedure.


def init():
    """Initializes all domaindata objects needed by the application.
    Each object can then be accessed direct or by using the provided 
    interface.
    """
    global _initialized, _loginUser, _domainContacts 

    if _initialized is True: return 

    if _loginUser is None: _loginUser = LoginUser()
    if _domainContacts is None: _domainContacts = DomainContacts()
    
    _initialized = True
    
def initialized():
    """Returns True if module has been initialized, else False
    """
    return _initialized

def set_proxy_environment(http_proxy = None, https_proxy = None, proxy_user = None, password = None):
    """Used to set the environment when being located behind an http proxy.
    """
    global _proxySettings
    _proxySettings = ProxySettings(http_proxy=http_proxy,
                                   https_proxy=https_proxy,
                                   proxy_user=proxy_user,
                                   password=password)


def set_login_credentials(email, password):
    global _loginUser, _domainContactsClient
    _loginUser.setFromEmail(email)
    _loginUser.password = password
    _domainContactsClient = DomainContactsClient(_loginUser)


def login():
    """Login at the google (apps) account with the provided credentials.
    """
    _domainContactsClient.loginAtSource()


def download_contacts():
    """Downloads all contacts found on google for gmail.com accounts and shared contacts
    for any other domain.
    """
    if _domainContactsClient:
        feedUrl = _domainContactsClient.GetFeedUri(contact_list=_loginUser.domain, 
                                         projection='full')
        while True:
            feed = _domainContactsClient.get_feed(uri=feedUrl,
                                                    auth_token=None,
                                                    desired_class=gdata.contacts.data.ContactsFeed)
            
            for entry in feed.entry:
                _domainContacts.append( DomainContact(entry) )
            
            next_link = feed.GetNextLink()
            # break
            if next_link is None:
                break
            else:
                feedUrl = next_link.href
          
        # import pickle
        # db = open("dsce.db","w+")
        # pickle.dump(_domainContacts, db)
        # db.close()

def get_contacts():
    """Used to return the current DomainContacts list.
    """
    return _domainContacts

def publish_changes():
    """Publish changes made to the contact
    """
    for c in _domainContacts.getChangedContacts():
        if c.getAction() == ACTION.UPDATE:
            logging.debug("Updated contact %s" % c.getFamilyName())
            _domainContactsClient.updateContact(c)
            # clear the action flag
            c.clearAction()


def get_action_summary():
    return _domainContacts.getActionSummary()

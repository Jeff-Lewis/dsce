# Abstract #

This page provides information about how to configure the **DomainSharedContactsEditor**.



# Configuration File #

The configuration `etc/dsce.json` is located within the installation directory. Under the same directory there can be found also two example configurations:
  * `noproxy.dsce.json.example` - Example syntax if you are behind a web proxy.
  * `proxy.dsce.json.example`  - Example syntax if you are **not** behind a web proxy.

The main reason to use it is to save your web proxy setting so that you have not to type them in at each logon. To do so copy the `proxy.dsce.json.example` over `dsce.json` and set the appropriate parameter values.

The configuration file uses the _JavaScript Object Notation_ do describe the configuration. For an introduction on JSON please refer to http://json.org.

# What read next? #

[How to support the project](http://www.dsce.org/how-to-support-the-project)
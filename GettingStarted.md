# Abstract #

This page provides information about the types of existing **DomainSharedContacsEditor-packages**, and how to install and use them.



# Basic Information #

The DomainSharedContacts client program is a python script that can be obtained
> A) as a source package,<br>
<blockquote>B) as a full developer source package,<br>
C) as a windows executable or<br>
D) as a local clone of the dsce mercurial repository.<br></blockquote>

The following table describes the content of each package type and under what file name convention it can be identified. In the file names <code>VERSION</code> must be replaced by the current version number like e.g. <code>0.0.0</code> or <code>0.0.0dev</code>.<br>
<br>
<table><thead><th></th><th> <b>Package</b> </th><th> <b>File name</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> A </td><td> source package </td><td> <code>dsce-VERSION.tar.gz</code> </td><td> Contains all source files and data, that are needed to run the program. This package does not contain required external modules. </td></tr>
<tr><td> B </td><td> full developer source </td><td> <code>dsce-dev-VERSION.tar.gz</code></td><td> This package is basically a compressed archive of the repository. It includes all source files including those just needed in the development process. It does not include required external modules.</td></tr>
<tr><td> C </td><td> windows executable </td><td> <code>dsce-VERSION-Windows.zip</code> </td><td> This package is the Microsoft windows executable of the program and contains everything that is needed to run the program. </td></tr></tbody></table>

Please follow the appropriate installation instructions according your package.<br>
<br>
<h1>Installation</h1>
<h2>Installation of A,B and D</h2>


If you want to use one of the source package variants (A,B,D) your system has to meet the following requirements:<br>
<br>
<ul><li><b>Python</b> 2.6 has to be installed on your system.</li></ul>

<ul><li>The script further requires the <b>GData Python client library</b> version 2.0.6 or higher which you can<br>
<ul><li>download from <a href='http://code.google.com/p/gdata-python-client/downloads/list'>http://code.google.com/p/gdata-python-client/downloads/list</a> and<br>
</li><li>install by following the Installation procedure described at <a href='http://code.google.com/apis/gdata/articles/python_client_lib.html'>http://code.google.com/apis/gdata/articles/python_client_lib.html</a>.</li></ul></li></ul>

<ul><li>Also the <b>wxPython</b> 2.8.11.0 or higher is required. To download and install the package please follow the instructions on <a href='http://www.wxpython.org/download.php'>http://www.wxpython.org/download.php</a></li></ul>

<i>As for the operating system any can be used as long as it can fulfill the requirements which means that BSD</i>, <i>Linux</i>, <i>!MaxOS X</i>, and <i>MSW</i> should work fine.<br>
<br>
To install the package just extract the package in a preferred directory on your system.<br>
<br>
<i>If you have cloned the repository you'll have to copy one of the example configuration files (depending whether you are behind a proxy or not) located in</i> <code>dsce*/etc/</code> <i>to</i> <code>dsce*/etc/dsce.json</code> <i>and adopt it to your needs.</i>

You can run the program by calling the <b>DomainSharedContactsEditor.py</b> script e.g.<br>
<br>
<code>python DomainSharedContactsEditor.py</code>


<h2>Installation of C</h2>

If you want to install and use the windows executable package it is enough to extract the package to a directory of your choice and start <b>DomainSharedContactsEditor.exe</b>.<br>
<br>
<h1>Configuration</h1>

Within the installation directory the file <code>etc/dsce.json</code> is the main configuration file of the <b>DomainSharedContactsEditor</b>.<br>
<br>
<br>
<h1>What read next?</h1>
<a href='Configuration.md'>How to configure the program</a>

<a href='Contribute.md'>How to support or contribute to the project</a>
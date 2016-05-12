deviantart 0.1.4
================

'deviantart' is a python package that provides easy access to the deviantart API.


Installation
------------

Installation using ``pip``::

    pip install -e git+git://github.com/SolimrUA/deviantart#egg=deviantart

Or, you wish to install original repository::

    pip install deviantart

Documentation
-------------

The documentation for this package can be found under: https://neighbordog.github.io/deviantart/

Be aware that for this fork documentation can be extremely outdated because I don't have intention to update it.

Basic usage
-----------

.. code:: python

   #import deviantart library
   import deviantart

   #create an API object with your client credentials
   da = deviantart.Api("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")

   #fetch daily deviations
   dailydeviations = da.browse_dailydeviations()

   #loop over daily deviations
   for deviation in dailydeviations:

       #print deviation title
       print(deviation.title)

       #print username of author of deviation
       print(deviation.author.username)


License
-------

The deviantart python package is licensed under the `MIT license
<https://opensource.org/licenses/MIT>`_.

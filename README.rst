=======================
JPush API Python Client
=======================

JPush's officially supported Python client library for accessing JPush APIs. 

JPush Rest API Documents: http://docs.jpush.io/server/rest_api_v3_push/

You can download the latest release file here: https://github.com/jpush/jpush-api-python-client/releases

------------
Installation
------------
To install jpush-api-python-client, simply:

    $ sudo pip install jpush

or alternatively install via easy_install:

    $ sudo easy_install jpush


or from source:

    $ sudo python setup.py install

-------
Testing
-------
For running the tests, you need the standard `unittest` module, shipped
with Python. 

To run jpush-api-python-client tests, simply:

    $ nosetests tests/push tests/devices --verbosity=2 

--------
Examples
--------
    You can see more examples in https://github.com/jpush/jpush-api-python-client/blob/master/examples

Simple iOS Push
---------------
    >>> import jpush as jpush
    >>> from conf import app_key, master_secret
    >>> _jpush = jpush.JPush(app_key, master_secret)
    >>> push = _jpush.create_push()
    >>> push.audience = jpush.all_
    >>> ios_msg = jpush.ios(alert="Hello, IOS JPush!", badge="+1", sound="a.caf", extras={'k1':'v1'})
    >>> android_msg = jpush.android(alert="Hello, android msg")
    >>> push.notification = jpush.notification(alert="Hello, JPush!", android=android_msg, ios=ios_msg)
    >>> push.options = {"time_to_live":86400, "sendno":12345,"apns_production":True}
    >>> push.platform = jpush.platform("ios")
    >>> push.send()


Get taglist
-----------------
    >>> import jpush as jpush
    >>> from conf import app_key, master_secret
    >>> _jpush = jpush.JPush(app_key, master_secret)
    >>> device = _jpush.create_device()
    >>> device.get_taglist()

--------
Questions
--------
The best place to ask questions is our community site:
http://community.jpush.cn/

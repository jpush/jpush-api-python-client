Examples
========

Common setup:

.. code-block:: python

   import jpush as jpush
   jpush = jpush.JPush(app_key, master_secret)

Simple broadcast to all devices
-------------------------------

.. code-block:: python

   push = jpush.create_push()
   push.audience = jpush.all_
   push.notification = jpush.notification(alert="Hello, world!")
   push.device_types = jpush.all_
   push.send()


Complex audience with iOS & Android specifics
---------------------------------------------

.. code-block:: python

   push = jpush.create_push()
   push.audience = jpush.audience(
      jpush.tag("breakingnews"),
      jpush.tag_and("sports"),
      )
   )
   push.notification = jpush.notification(
      ios=jpush.ios(
         alert="Kim Jong-Un wins U.S. Open",
         badge="+1",
         extra={"articleid": "123456"}
      ),
      android=jpush.android(
         alert="Breaking Special Android News! Glorious Leader Kim Jong-Un wins U.S. Open!",
         extra={"articleid": "http://m.example.com/123456"}
      )
   )
   push.platform = jpush.platform('ios', 'android')
   push.send()


Single iOS push
---------------

.. code-block:: python

   push = jpush.create_push()
   push.audience = jpush.registration_id('fffffffffff')
   push.notification = jpush.notification(
       ios=jpush.ios(alert="Kim Jong-Un is following you on Twitter"))
   push.platform = jpush.platform('ios')
   push.send()

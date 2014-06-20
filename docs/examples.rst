Examples
========

Common setup:

.. code-block:: python

   import jpush as jpush
   _jpush = jpush.JPush(app_key, master_secret)

Simple broadcast to all devices
-------------------------------

.. code-block:: python

   push = _jpush.create_push()
   push.audience = jpush.all_
   push.notification = jpush.notification(alert="Hello, world!")
   push.platform = jpush.all_
   push.send()


Complex audience with iOS & Android specifics
---------------------------------------------

.. code-block:: python

   push = _jpush.create_push()
   push.audience = jpush.audience(
      jpush.tag("breakingnews"),
      jpush.tag_and("sports"),
      )
   )
   push.notification = jpush.notification(
      ios=jpush.ios(
         alert="JPush ios test",
         badge="1",
         extras={"articleid": "123456"}
      ),
      android=jpush.android(
         alert="Breaking Special Android News!",
         extras={"articleid": "http://m.example.com/123456"}
      )
   )
   push.platform = jpush.platform('ios', 'android')
   push.send()


Single iOS push
---------------

.. code-block:: python

   push = _jpush.create_push()
   push.audience = jpush.registration_id('fffffffffff')
   push.notification = jpush.notification(
       ios=jpush.ios(alert="JPush powers your apps"))
   push.platform = jpush.platform('ios')
   push.send()

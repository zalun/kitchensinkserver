=================
Development Notes
=================

Sructure
########
Uniqueness
----------
We don't want to have multiple identical submits from the same phone. It needs 
to be unique in the system. App will retrieve an id after user will agree to 
send data to the collection server. It will be stored on the phone.

Devices
-------
Since there is no way of retrieving information about the phone, we ask the 
user to choose this info from a list. There is a need for an API to GET and UI
to provide this info. We should also consider PUSH for users to be able to add
non standard devices.

System
------
We will get data from FxOS and Android. These will be in different versions

App
---
Tests will change and it might happen that a test result will change for the
same device in the same software version.

Test results
------------
APIs will be added and possibly removed. there might be more than one test per
API. Mintaining the database structure might be complicated - we should 
consider using text database (Redis?).


API
###

We are using tastypie.

phone/
------
GET only
will create a unique id and return

device/
-------
GET
LIST

PUSH Depends on our choice

result/
-------
GET
PUSH

Stored in non relational database
Result will connect phone, device and will contain test data
We should be able to retrieve statistical information by device, time

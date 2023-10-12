# MD3

## Manage Musics MetaData.

## MP3 Tag MetaData ( **MD3** )

Create CSV Musics MetaData.

Set & Get MP3 MetaData.

It can find all MP3 files in the path you entered, also **+Recursivly**.

Save all MP3 MetaData in CSV file, then you can edit the CSV file.

And you can update your MP3 MetaData(set MetaData) from the edited CSV file.

It will be very good if anybody can help me to develop and extend this application.

## Installation: in Python3

install python3 and some python modules:

in Debian base :

    $ sudo apt-get install python

    $ pip install pathlib CSV eyed3 pprint glob2 re

in Redhat base :

    $ su -

    # subscription-manager repos --enable rhel-7-server-optional-rpms \

      --enable rhel-server-rhscl-7-rpms

    # yum -y install @development

    # yum -y install rh-python36

then run :

    $ python md3.py

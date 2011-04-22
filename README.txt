Usage
=====

Add FightForNetNeutrality to your python path using ``easy_install``::

  $ easy_install FightForNetNeutrality

Then wrap your wsgi application with the fightfornetneutrality.NetNeutrality middleware::

  from fightfornetneutrality import NetNeutrality
  application = NetNeutrality(application)

You can also define your own IP range::

  application = NetNeutrality(application, ips_banned={"62.160.71.0":24})

That's it.


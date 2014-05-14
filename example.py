#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tinder, datetime

# Encoding to UTF8 so it displays correctly in console
def uniutf(t):
	return t.encode('utf-8')

# Used to get the age from a birthdate
def age(born):
    today = datetime.datetime.strptime(datetime.datetime.utcnow().isoformat()[:10], "%Y-%m-%d").date()
    born = datetime.datetime.strptime(born[:10], "%Y-%m-%d").date()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# The Facebook token and user's ID
fbToken = {
	'facebook_token': '',
	'facebook_id': ''
}

# Creating instance of class Tinder
tinder = tinder.tinderClient(fbToken)

# Getting nearby users (Tinder will send 10)
nearby = tinder.get_recs()

# Let's get and print some informations about those nearby users
try:
	for rec in nearby['results']:
		print "Name: %s" % uniutf(rec['name'])
		print "Photo: %s" % rec['photos'][0]['url']
		print "Age: %s" % age(rec['birth_date'])
		print "Distance: %s %s" % (rec['distance_mi'], "miles" if int(rec['distance_mi']) > 1 else "mile")
		print "==="
except KeyError:
	print nearby['message']
	pass
except:
    import traceback
    print "Error: %s" % traceback.format_exc()
    pass

"""
Example output:

	Name: Clara
	Photo: http://images.gotinder.com/5365fbc18415d24d69004c85/7ca67882-ff2b-4af8-8f89-1ff777447cf5.jpg
	Age: 20
	Distance: 93 miles
	===
	Name: Emilie
	Photo: http://images.gotinder.com/536b8fdf816c5fa910000429/7a18f554-dea8-4927-8d30-c0873c69b73d.jpg
	Age: 20
	Distance: 84 miles
	===
	Name: Eléonore
	Photo: http://images.gotinder.com/53409ea207f71bdf06001dd9/ebc7c161-6754-4279-9d7b-09080f3b1b26.jpg
	Age: 108
	Distance: 92 miles
	===
	Name: Léa
	Photo: http://images.gotinder.com/53681581f27aa87903009797/d226f076-a8f9-4e2c-8178-dc8ca5588440.jpg
	Age: 18
	Distance: 80 miles
	===
	Name: Floriane
	Photo: http://images.gotinder.com/536a6ce0e0200e8f6800e0c9/f5865888-b61d-432e-bbc3-64afe003e732.jpg
	Age: 18
	Distance: 94 miles
	===
	Name: Roxanne
	Photo: http://images.gotinder.com/536e87b8c10a43ef710011a7/22ec8ba1-5d2d-43aa-8d56-a81bf34f1a61.jpg
	Age: 18
	Distance: 93 miles
	===
	Name: Laurie
	Photo: http://images.gotinder.com/5365428fec24cc156900321f/7574024d-3cd9-4cea-8be8-444d7bd62c2f.jpg
	Age: 18
	Distance: 58 miles
	===
	Name: Erin
	Photo: http://images.gotinder.com/536ed112452df94f5a001e15/725201a4-22d7-423b-8366-03e81531e032.jpg
	Age: 20
	Distance: 83 miles
	===
	Name: Anais
	Photo: http://images.gotinder.com/534c6965f293bac322006d4d/1794c2f0-f40d-4d2d-8c07-c1261f69accb.jpg
	Age: 19
	Distance: 99 miles
	===
	Name: Jessica
	Photo: http://images.gotinder.com/535397d3c0ba97e125001331/ad232b37-2938-44ce-8875-af070ab9bc9b.jpg
	Age: 19
	Distance: 92 miles
	===
	Name: Salomé
	Photo: http://images.gotinder.com/536febc6ea1e0a120c0019f1/13bed851-59a1-46ef-b4bf-85bdea64ace7.jpg
	Age: 108
	Distance: 78 miles
	===
	[Finished in 0.8s]
"""

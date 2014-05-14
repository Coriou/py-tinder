#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib2, datetime, string

class tinderClient():
	tinderApi = "https://api.gotinder.com/"
	timeOut = 3
	token = None
	location = None
	headers = None
	authHeaders = None
	lastUrl = None
	lastError = None
	appVersion = None
	osVersion = None

	def __init__(self, token, location = {'lat': '48.856614', 'lon': '2.352222'}, tinderVersion='3.0.4', iosVersion = '7.1'):

		self.version(tinderVersion, iosVersion)

		self.authHeaders = {
			'Accept-Language': 'fr;q=1, en;q=0.9, de;q=0.8, zh-Hans;q=0.7, zh-Hant;q=0.6, ja;q=0.5',
			'User-Agent': 'Tinder/'+tinderVersion+' (iPhone; iOS '+iosVersion+'; Scale/2.00)',
			'os_version': self.osVersion,
			'Accept': '*/*',
			'platform': 'ios',
			'Connection': 'keep-alive',
			'app_version': self.appVersion,
			'Accept-Encoding': 'gzip, deflate'
		}

		try:
			if (isinstance(token, str)):
				try:
					self.token = self.auth(json.loads(token))['token']
				except:
					self.token = token
			else:
				self.token = self.auth(token)['token']
		except:
			self.errorLogger('Auth', 'Error while getting authentication token')

		self.location = location
		self.headers = self.authHeaders
		self.headers['X-Auth-Token'] = self.token
		self.headers['Authorization'] = 'Token token="%s"' % (self.token)

	"""The GET method for the client
	Used for: recs, user, like, pass"""
	def get(self, uri):
		headers = self.headers
		url = self.lastUrl = self.url(uri)
		try:
			r = urllib2.Request(url, headers=headers)
			return json.loads(urllib2.urlopen(r, timeout=self.timeOut).read())
		except urllib2.HTTPError, e:
			return self.errorLogger('HTTP', e.code)
		except urllib2.URLError, e:
			return self.errorLogger('URL', e.code)
		except Exception:
		    import traceback
		    return self.errorLogger('generic', traceback.format_exc())

	"""The POST method for the client
	Used for: auth, ping, update"""
	def post(self, uri, data):
		if (uri == 'auth'):
			headers = self.authHeaders
		else:
			headers = self.headers
		headers['Content-Type'] = 'application/json; charset=utf-8'
		data = json.dumps(data)
		url = self.lastUrl = self.url(uri)
		try:
			r = urllib2.Request(url, data=data, headers=headers)
			return json.loads(urllib2.urlopen(r, timeout=self.timeOut).read())
		except urllib2.HTTPError, e:
			return self.errorLogger('HTTP', e.code)
		except urllib2.URLError, e:
			return self.errorLogger('URL', e.code)
		except Exception:
		    import traceback
		    return self.errorLogger('generic', traceback.format_exc())

	"""Authentication method of the client
	Better not to call it directly unless you know what you're doing
	Is called upon __init__ to get the auth token"""
	def auth(self, fbToken):
		return self.post('auth', fbToken)

	"""Returns user's Tinder profile"""
	def get_profile(self):
		return self.get('profile')

	"""Updates user's settings
	Variables:
		distance_filter: [2,160]
		gender: [0,1] (male, female)
		age_filter_min: 18
		age_filter_max: 1000
		gender_filter: [-1, 0, 1] (males & females, males, females)
		bio: String"""
	def post_profile(self, data):
		return self.post('profile', data)

	"""Returns nearby users
	Error messages:
		recs timeout: did not find nearby users quick enough
		recs exhausted: no more users nearby right now"""
	def get_recs(self):
		return self.get('user/recs')

	"""Pings Tinder's servers
	Also used to pass the geolocation"""
	def post_ping(self):
		return self.post('user/ping', self.location)

	"""Gives last updates since lastActivty (matches, messages, ...)
	If lastActivty is invalid (0 or 1 for instance) it will give you all updates"""
	def post_updates(self, lastActivity = None):
		if lastActivity is None:
			lastActivity = datetime.datetime.utcnow().isoformat()
		data = {'last_activity_date': lastActivity}
		return self.post('updates', data)	

	"""Likes uid
	Returns match: true/false"""
	def get_like(self, uid):
		return self.get('like/%s' % (uid))

	"""Dislikes uid"""
	def get_pass(self, uid):
		return self.get('pass/%s' % (uid))

	"""Gets all informations for user uid"""
	def get_user(self, uid):
		return self.get('user/%s' % (uid))

	"""Formats the API's url"""
	def url(self,u):
		return "%s%s" % (self.tinderApi, u)

	"""Unicode to UTF8 used to debug in console"""
	def uniutf(t):
		return t.encode('utf-8')

	"""Sends a ping with lat and lon as geolocation
	If you "move" too quick Tinder will notice it"""
	def updateLocation(self, lat, lon):
		self.location['lat'] = lat
		self.location['lon'] = lon
		return self.post_ping()

	"""Catches errors and returns them
	Last error also stored in self.lastError"""
	def errorLogger(self, Etype, data):
		e = {'error': 1, 'type': Etype, 'errorData': data, 'url': self.lastUrl, 'headers': self.headers}
		e = self.lastError = json.dumps(e)
		return e

	"""Formats Tinder's and iOS's version correctly for headers
		Example Tinder version: 3.0.4
		Example iOS version: 7.1"""
	def version(self, tinder, ios):
		tV = string.split(tinder, '.')
		self.appVersion = tV[0]

		tI = filter(None, string.split(ios, '.'))
		tL = (5 - (len(tI) -1))
		self.osVersion = tI[0] + ('0' * ((tL/len('0'))+1))[:tL] + ''.join(tI[1:len(tI)])
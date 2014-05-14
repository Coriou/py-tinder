py-tinder
==============

A python wrapper for Tinder's API
--------------

This is my first python project, code might not be well optimized so feel free to fork it and make it better, add features etc…

Current features
--------------

- Auth
- Get user profile
- Update user profile
- Get users nearby
- Ping / update location
- Get last updates (messages, matches, …)
- Like a profile
- Pass a profile

Missing features
--------------

- Messages

Code improvements needed
--------------

- The client needs a proper error handling system

Basic usage
--------------

	fbToken = {
		'facebook_token': ‘XXX’,
		'facebook_id': ‘XXX’
	}
	tinder = tinder.tinderClient(fbToken)
	nearby = tinder.get_recs()

If you have the actual token from Facebook already, you can use it directly (but it will expire eventually):

	fbToken = ‘XXX-XXX-XXX’
	tinder = tinder.tinderClient(fbToken)
	nearby = tinder.get_recs()
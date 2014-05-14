#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tinder, argparse, json

parser = argparse.ArgumentParser()
parser.add_argument("--action", "-a", help="What to do [updates|recs|profile|ping|location|like|pass|user|token]", type=str, required=True)
parser.add_argument("--data", "-d", help="JSON data to pass as argument", type=str)
parser.add_argument("--token", "-t", help="The Facebook token / id pair or just the auth token", type=str, required=True)

args = parser.parse_args()

if args.action == 'updates':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	print json.dumps(tinder.post_updates())

if args.action == 'recs':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	print json.dumps(tinder.get_recs())

if args.action == 'profile':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	if not args.data:
		print json.dumps(tinder.get_profile())
	else:
		data = json.loads(args.data)
		print json.dumps(tinder.post_profile(data))

if args.action == 'ping':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	print json.dumps(tinder.post_ping())

if args.action == 'location':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	data = json.loads(args.data)
	print json.dumps(tinder.updateLocation(data['lat'], data['lon']))

if args.action == 'like':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	data = json.loads(args.data)
	print json.dumps(tinder.get_like(data['uid']))

if args.action == 'pass':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	data = json.loads(args.data)
	print json.dumps(tinder.get_pass(data['uid']))

if args.action == 'user':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	data = json.loads(args.data)
	print json.dumps(tinder.get_user(data['uid']))

if args.action == 'token':
	fbToken = args.token
	tinder = tinder.tinderClient(fbToken)
	print json.dumps({'token': tinder.token})

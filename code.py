#!/usr/bin/env python
# coding: utf-8
from config.url import urls
import web

app = web.application(urls, globals())

if web.config.get('_session') is None:
	session = web.session.Session(app, web.session.DiskStore('sessions'), initializer = {'login': 0,'userid':'0'})
	web.config._session = session
else:
	session = web.config._session

if __name__ == "__main__":
    app.run()
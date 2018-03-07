import web

urls = ('/','index')

class index:
	def GET(self):
		return 'is was work'

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()

import web

urls = (
    '/', 'Index',
    '/talleres', 'Talleres',
    '/referencias', 'Referencias',
    '/contacto','Contacto',
	'/amistad', 'Amistad',
    '/ansiedad', 'Ansiedad',
    '/depresion', 'Depresion',
    '/hobby', 'Hobby',
    '/terapia', 'Terapia',
)

app = web.application(urls, globals())
wsgiapp = app.wsgifunc()
render = web.template.render('templates/')

class Index:
	def GET(self):
		return render.index()

class Talleres:
	def GET(self):
		return render.talleres()

class Referencias:
	def GET(self):
		return render.referencias()

class Contacto:
	def GET(self):
		return render.contacto()

class Ansiedad:
	def GET(self):
		return render.ansiedad()

class Amistad:
	def GET(self):
		return render.amistad()

class Depresion:
	def GET(self):
		return render.depresion()

class Hobby:
	def GET(self):
		return render.hobby()

class Terapia:
	def GET(self):
		return render.terapia()


if __name__ == "__main__": 
    web.config.debug = False
    app.run()

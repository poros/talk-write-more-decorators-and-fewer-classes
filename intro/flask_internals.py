class Flask(_PackageBoundObject):
	def route(self, rule, **options):
		def decorator(f):
			endpoint = options.pop('endpoint', None)
			self.add_url_rule(rule, endpoint, f, **options)
			return f
		return decorator

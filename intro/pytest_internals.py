def fixture(scope="function", params=None, autouse=False, ids=None, name=None):
	if callable(scope) and params is None and autouse == False:
			# direct decoration
			return FixtureFunctionMarker(
					"function", params, autouse, name=name)(scope)
	if params is not None and not isinstance(params, (list, tuple)):
			params = list(params)
	return FixtureFunctionMarker(scope, params, autouse, ids=ids, name=name)


class FixtureFunctionMarker:
    def __init__(self, scope, params, autouse=False, ids=None, name=None):
        self.scope = scope
        self.params = params
        self.autouse = autouse
        self.ids = ids
        self.name = name

    def __call__(self, function):
        if isclass(function):
            raise ValueError(
                    "class fixtures not supported (may be in the future)")
        function._pytestfixturefunction = self
		return function

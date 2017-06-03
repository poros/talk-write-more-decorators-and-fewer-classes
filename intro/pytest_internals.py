def fixture(scope="function", params=None, autouse=False, ids=None, name=None):
	if callable(scope) and params is None and autouse == False:
			# direct decoration
			return FixtureFunctionMarker(
					"function", params, autouse, name=name)(scope)
	if params is not None and not isinstance(params, (list, tuple)):
			params = list(params)
	return FixtureFunctionMarker(scope, params, autouse, ids=ids, name=name)

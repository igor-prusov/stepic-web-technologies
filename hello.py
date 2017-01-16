def application(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-type', 'text/plain')
	]
	query_str = str(environ['QUERY_STRING'])
	body = query_str.replace('&', '\n')
	start_response(status, headers)
	return [body]

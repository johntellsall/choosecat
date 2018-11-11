import choosecat

def test_hello():
	response = choosecat.hello_world(request=None)
	assert 'Hello' in response.text

def test_database():
	assert choosecat.check_database() == 'blam'

del test_database # TODO

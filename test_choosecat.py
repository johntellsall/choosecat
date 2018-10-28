import choosecat

def test_hello():
	response = choosecat.hello_world(request=None)
	assert 'Hello' in response.text

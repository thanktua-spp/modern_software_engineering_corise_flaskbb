###################################################################
# CoRise TODO: add an integration test that uses the test client to
# load the home page ('/'). Make sure the response code is 200 and
# that the response data contains something you expect to see on the
# home page.
#
# Hint: you can get the test client by calling `application.test_client()`
# when using the application test fixture.

# ADD CODE HERE
def test_index_route(application, default_settings, default_groups, default_translations):
    with application.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Forum" in response.data
        assert b"Portal" in response.data
###################################################################
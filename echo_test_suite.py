import validate_expected_response, get_request, validate_no_response


def test_get_request(http_server, http_client):
    print("STEP 1: Send GET request and validate response status is ok and 200")
    validate_expected_response(get_request(http_client))
    print("STEP 2: Stop http server, send GET request and validate there is no response")
    http_server.close_server()
    validate_no_response(get_request(http_client))

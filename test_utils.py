# Test Utilities:
# - http server: create a server that contains "start" and "stop" functions
# - http client: create and close a client connection to the created http server
# - send a request: send a "get" request to the server and return the response
# - Validation functions: validate response and no response
import http.client
import pytest
import my_server


@pytest.fixture()
def http_server():
    server = my_server.ServerHttpUtils()
    server.create_server()
    yield server 
    print("ClenUp")
    server.close_server()


@pytest.fixture()
def http_client(http_server):
    connection = http.client.HTTPConnection(http_server.SERVER_HOST, http_server.SERVER_PORT, timeout=10)
    yield connection
    print("ClenUp")
    connection.close()


def get_request(http_client):
    try:
        print("Sending GET request...")
        http_client.request("GET", "/")
        return http_client.getresponse()
    except ConnectionRefusedError:
        return False


def validate_expected_response(response):
    if response:
        if response.status != 200 or response.reason != "OK":
            pytest.fail(f"response result is:\nStatus: {response.status} and Reason: {response.reason} "
                        f"\nnot as expected: Status: 200 and reason: OK")
        else:
            print("PASS: Status: {} and reason: {} as expected".format(response.status, response.reason))
    else:
        pytest.fail("There is NO response!")


def validate_no_response(response):
    if response:
        print("Status: {} and reason: {}".format(response.status, response.reason))
        pytest.fail("Got a response! Not as expected!")
    else:
        print("PASS: There is no response, as expected")

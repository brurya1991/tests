import http.client
import pytest

import my_server


@pytest.fixture()
def http_server():
    server = my_server.ServerHttpUtils()
    server.create_server()
    yield server
    server.close_server()


@pytest.fixture()
def http_client(http_server):
    connection = http.client.HTTPConnection(http_server.SERVER_HOST, http_server.SERVER_PORT, timeout=10)
    yield connection
    connection.close()


def send_request(http_client):
    try:
        http_client.request("GET", "/")
        response = http_client.getresponse()
    except ConnectionRefusedError:
        return False
    return response


def validate_expected_response(response):
    if response:
        print("Status: {} and reason: {}".format(response.status, response.reason))
        if response.status != 200 or response.reason != "OK":
            pytest.fail(f"response result is:\nStatus: {response.status} and Reason: {response.reason} "
                        f"\nnot as expected: Status: 200 and reason: OK")
    else:
        pytest.fail("There is NO response!")


def validate_no_response(response):
    if response:
        print("Status: {} and reason: {}".format(response.status, response.reason))
        pytest.fail("Got a response! Not as expected!")
    else:
        print("There is NO response as expected")


def test_send_request(http_server, http_client):
    validate_expected_response(send_request(http_client))
    http_client.close()
    http_server.close_server()
    validate_no_response(send_request(http_client))

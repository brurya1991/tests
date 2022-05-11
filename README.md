# HTTP Test:
## Test resurces: 
### my_server.py:
#### create the http server with it's functions (e.g. create, start, stop server)
### test utils: 
####   1. Setup: create server and client and cleanUp (close it)
####   2. Action: send GET request and return the response
####   3. Validation: validate response status and no response 
## Test echo_test_suite.py steps:
###    1. Tests sending GET requests to the server and validating the status code of the response
###    2. Tests shutting down the echo server and sending GET requests to the server then validating that no response was received
## Test trigger: 
### pytest command specified in pylint.yml (pyton 3.9) trigged by commit action

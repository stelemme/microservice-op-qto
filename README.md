# QTO (Quantity Takeoff) Operation Microservice

## Installation

To install this Microservice, make sure Python 3.9 or higher is installed on your device. Installing the Microservice can be done by first starting a Python virtual environment and then installing the dependencies stored in the [pyproject.toml](https://github.com/stelemme/microservice-op-qto/blob/main/pyproject.toml) file. The virtual environment is activated using the following commands.
```
python -m venv .venv
.venv\Scripts\activate
```
The Microservice can now be installed using the following command.
```
pip install -e .
```
## Running the Microservice
To run the Microservice, a virtual environment needs to be activated using the following command.
```
.venv\Scripts\activate
```
After the virtual environment is activated the Microservice can be run using the following command. Additional arguments can be added to the command to for example run the Microservice in debug mode (--debug), which enables live reloading. The port on which the Microservice runs can also be changed with an additional argument (--port <port-number>).
```
flask --app flaskr run
```
## Using the Microservice
The functionality of this Microservice can be acces via the following endpoint.
  
[http://localhost:5000/op/qto](http://localhost:5000/op/qto)
  
This endpoint has a GET and POST method. The GET response of the endpoint returns a JSON object that specifies which methods are supported by the endpoint, in this case a GET and POST method. The JSON object also specifies the data type each method accepts and returns (given as its MIME type). For this endpoint, an LBD-file, given in the Turtle (Terse RDF Triple Language) syntax which expresses the Resource Description Framework (RDF) format, must be sent in a POST request to the endpoint. The endpoint then returns a JSON-LD file with the calculated QTO. This process can be tested using Postman or a Controller Microservice.

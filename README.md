# League Backend challenge
Submission for a League Inc's backend challenge by Rotola Akinsowon. This challenge was completed with python


## Contents
* [Requirements & Setup](#Requirements-&-Setup)
* [Running The App](#running-the-app)
* [Task Description](#task-description) 


## Requirements & Setup
Listed below are the core requirements of the application
- [Python 3.8](https://www.python.org/downloads/release/python-380/) or higher
- [PIP 3](https://pip.pypa.io/en/stable/installation/) - Typically present with your python installation, if not you 
  can install following the guide
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)

### Setup
This app was built and tested on Ubuntu Linux, but the scripts should be compartible with most unix based systems.
A one-time setup is required in other to run the app properly, this is done by running the following command
  ```shell
  # from the apps root dir in a bash shell
  ./run init
  ```

## Running The App
After succesfully initializing the app, you're now ready to run the app.
The server is started with 

```shell
./run start

# the application runs on port 8083 by default but you can specify a port using
PORT=8091 ./run start

```
A request can be sent using curl like so:

```shell
# from the apps root dir in a bash shell
curl -F 'file=@fixtures/valid.csv' "http://localhost:8083/invert"

# from any other path in a bash shell
curl -F 'file=@path/to/csv' "http://localhost:8083/invert"

```

Tests are run using

```shell
./run test

```

## Task Description

In main.go you will find a basic web server written in GoLang. It accepts a single request _/echo_. Extend the webservice with the ability to perform the following operations

Given an uploaded csv file
```
1,2,3
4,5,6
7,8,9
```

1. Echo (given)
    - Return the matrix as a string in matrix format.
    
    ```
    // Expected output
    1,2,3
    4,5,6
    7,8,9
    ``` 
2. Invert
    - Return the matrix as a string in matrix format where the columns and rows are inverted
    ```
    // Expected output
    1,4,7
    2,5,8
    3,6,9
    ``` 
3. Flatten
    - Return the matrix as a 1 line string, with values separated by commas.
    ```
    // Expected output
    1,2,3,4,5,6,7,8,9
    ``` 
4. Sum
    - Return the sum of the integers in the matrix
    ```
    // Expected output
    45
    ``` 
5. Multiply
    - Return the product of the integers in the matrix
    ```
    // Expected output
    362880
    ``` 

The input file to these functions is a matrix, of any dimension where the number of rows are equal to the number of columns (square). Each value is an integer, and there is no header row. matrix.csv is example valid input.  

Run web server
```
go run .
```

Send request
```
curl -F 'file=@/path/matrix.csv' "localhost:8080/echo"
```

### What we're looking for

- The solution runs
- The solution performs all cases correctly
- The code is easy to read
- The code is reasonably documented
- The code is tested
- The code is robust and handles invalid input and provides helpful error messages
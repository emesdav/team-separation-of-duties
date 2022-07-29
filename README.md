# README #

### Purpose of the repository ###

As a part of the team 'Separation of Duties' in the 'Secure Software Development' (SSDCS_PCOM7E) module's coding-related 
assignment, this repository contains Python-based codes to run an application to perform CRUD operations in a 
GDPR-compliant manner. This application was developed considering the use case of aiding the Dutch Police Internet 
Forensics Unit by providing them with a secure repository.

### Setup ###

* Update conda

Update conda by executing the following command:

`conda update -n base -c defaults conda`

* Create the virtual environment

Create a conda virtual environment named `internet_forensics` and install the required dependencies by executing the 
following command: 

`conda env create --name internet_forensics --file environment.yml`

* Activate and deactivate the conda environment

To activate this environment, execute the following command:

`conda activate internet_forensics`

To deactivate the environment, execute the following command:

`conda deactivate`

* Data layer of the application

SQLite is used as CRUD operations need to be performed and their results need to be persisted in a relational database. 

### Description of the solution implemented ###

### Instruction to execute the solution ###

### Testing methodology ###

The following testing approaches have been adopted:
- **functional testing** throughout the development of the application and at the end of it to ensure the methods and 
  functions developed behave as expected;
- **regression testing** to ensure that, at every update of the application, existing functionalities still work as expected, 
  i.e., they are not compromised by adding new functionalities to the application;
- **unit testing** to verify that the logic of the functionalities implemented is correct and various cases (positive and 
  negative) are accounted for;
- **integration testing** to ensure that, given certain inputs, specific outputs are returned and their data types are also 
  matching the expected one/s.

### Running the tests ###

All tests can be run by executing `pytest tests`. To view the test coverage report too, execute: 
`pytest --cov=internet_forensics tests`.

#### Test coverage ####

### Future work ###

Future work will include:
- TBD
- TBD
- TBD

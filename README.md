# README #

### Purpose of the repository ###

As a part of the team 'Separation of Duties' in the 'Secure Software Development' (SSDCS_PCOM7E) module's coding-related 
assignment, this repository contains Python-based codes to run an application to perform 
[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations whilst complying 
with [GDPR](https://gdpr.eu/). This application was developed considering the use case of aiding the Dutch Police Internet 
Forensics Unit by providing them with a secure repository.

### Setup ###

* Update conda

Update conda by executing the following command:

`conda update -n base -c defaults conda`

some people are likely to run into an issue when running the above command for updating conda.

A known issue would be `"PackageNotInstalledError: Package is not installed in prefix."` In such case, the below command to update all and not selective appears to be an alternative solution. It may appear to be an overkill but works and you need to update all anyway.

`conda update --all`

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
- [**functional testing**](https://en.wikipedia.org/wiki/Functional_testing) throughout the development of the application and at the end of it to ensure the methods and 
  functions developed behave as expected;
- [**regression testing**](https://en.wikipedia.org/wiki/Regression_testing) to ensure that, at every update of the application, existing functionalities still work as expected, 
  i.e., they are not compromised by adding new functionalities to the application;
- [**unit testing**](https://en.wikipedia.org/wiki/Unit_testing) to verify that the logic of the functionalities implemented is correct and various cases (positive and 
  negative) are accounted for;
- [**integration testing**](https://en.wikipedia.org/wiki/Integration_testing) to ensure that, given certain inputs, specific outputs are returned and their data types are also 
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

### Team's rules regarding this repository ###

- Codes must not be merged directly to the `main` branch, but a feature or hotfix branch needs to be created for each 
functionality or fix of existing functionality.
- [Feature branches](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) should be named as `feature/` followed by a short hyphenated description of the purpose of the branch, 
e.g., `feature/write-readme` represents a feature branch to write the README.md file, whilst `hotfix/fix-readme` would 
indicate that a fix has been implemented to correct some information on the README.md file (the name of the branch could 
be made even more explicit, but it should be concise.).
- At least one approval is required before merging a pull request (PR). The developer/assignee who raised the PR is 
responsible for merging the PR once at least one approval is received.
- Coding standards: 
  - Any dependencies must be added to the `environment.yml` file, which must be kept up to date. Further channels to 
    install them could be added in this file, but `conda` is recommended and `pip` could be used if a library were not 
    available to be installed via `conda`.
  - Codes must have [docstrings and type hints](https://towardsdatascience.com/python-type-hints-docstrings-7ec7f6d3416b) 
    for ease of maintainability.
  - Codes must be [unit-tested](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/); 
    if a function were suggested to be excluded, e.g., as too trivial for it to be unit-tested, 
    an [appropriate marker](https://coverage.readthedocs.io/en/6.3.3/excluding.html) (e.g., `# pragma: no cover` as 
    defined in the file `.coveragerc`) should be placed beside it to indicate that the codes below a function or class 
    are excluded from the test coverage. This can be negotiated/discussed during code reviews.
  - Constants and utility-type of functions should be stored in `constants.py` and `utils.py` files under the relevant 
    directory within and/or under which they are leveraged for ease of maintainability and re-usability.
  - [Appropriate validation](https://automatetheboringstuff.com/2e/chapter8/) must be performed prior to ingesting any inputs.
    - An existing open-source and reputable library, e.g., '[schema](https://pypi.org/project/schema/)' or 
    '[cerberus](https://docs.python-cerberus.org/en/stable/)` for instance, may be used if it could avoid reinventing 
    the wheel. In cases wherein existing libraries did not support the required validation or it would be fast and 
    straightforward to implement own validation logic, custom codes would be welcome.
  - Unless multiple classes were related, e.g., via inheritance, etc., each file should contain one class for increased 
    modularity.
  - '[PEP-8](https://peps.python.org/pep-0008/)' should be adhered to.
  - Ideally, a [Python package-like structure](https://docs.python-guide.org/writing/structure/) should be followed to enable the application to be installed via `pip` and 
    to facilitate testing.

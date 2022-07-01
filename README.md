**How to Run This Program**
*Requirements*
- Python 3.8.*
- Pipenv
- Virtual Env
- Pytest

* Create and enter a virtual environment and run these commands within the virtual env

*Commands To Run*
- `pipenv install`  to install dependencies
- `pytest` to run the unit tests

--------------------------------------------------------------------------------------------------------------

**Currently this code only runs via unit tests. How might we run an operation like this in production, at scale?**

First, we would ensure that we have interfaces to receive input and return output. Next would be to ensure that these I/O processes are asynchronous calls and that the code is also running asynchronously. We would also implement better seperation of concerns eg. implementing OOP classes and functions for easier code reuse as well. We would also have to think about how and where the input and output data is stored; this could involve making use of databases, caching or temporary output files depending on our needs.

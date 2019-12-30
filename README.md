# Quoty -- store your favourite quotes
## Installation

1. Clone this repo.
2. Install dependencies. (For guide to use virtualenv, see [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/]())
    ```
        pip3 install -r requirements.txt
    ```
3. Add the following line to your .bashrc, replace the path with your own path (e.g. $HOME/quoty).
    ```
        export QUOTY_PATH=<path-to-quoty>
        alias quoty='python $QUOTY_PATH/quoty.py'
    ```
    For virtualenv, last line can be done as ```alias quoty='source <path-to-virtualenv> && python $QUOTY_PATH/quoty.py && deactivate'```

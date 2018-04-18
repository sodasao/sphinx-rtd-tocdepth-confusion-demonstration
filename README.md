# sphinx-rtd-tocdepth-confusion-demonstration
making a repo to demonstrate the issue

1. Create a virtual environment to test the latest master.

    ```console
    $ virtualenv venv

    $ source venv/bin/activate
    ```

2. Install the latest `master` branch of `sphinx_rtd_theme` (will also install
   latest stable version of sphinx).

    ```console
    (venv) $ pip install -r requirements.txt
    ```

3. Build the docs. `cd docs && make html` 

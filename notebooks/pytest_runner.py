# Databricks notebook source
# pytest_runner is a utility script that runs all the tests in the tests directory of a Databricks repository.
# The script installs pytest, switches to the root directory of the repository, and runs pytest.
# If any tests fail, the script raises an exception to fail the cell execution.

# COMMAND ----------

%pip install pytest
# COMMAND ----------

import pytest
import sys
import os

notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# Get the repo's root directory name.
dir_root = os.path.dirname(os.path.dirname(notebook_path))

# Switch to the root directory on databricks.
os.chdir(f"/Workspace/{dir_root}")

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."

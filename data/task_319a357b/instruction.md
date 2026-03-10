I'm an automation specialist setting up a new workflow project on my Linux machine. I have a project skeleton at `/home/user/automation_project` with a script that needs specific dependencies. I need you to set up a Python virtual environment and install the required packages so the project is ready to run.

Here's what I need done:

1. Create a Python virtual environment named `venv` inside `/home/user/automation_project/`. Use the `python3` command to create it.

2. Using the virtual environment's pip (at `/home/user/automation_project/venv/bin/pip`), install the following packages at these exact versions:
   - `requests==2.28.2`
   - `schedule==1.2.0`
   - `python-dotenv==1.0.0`

3. After installation, generate a frozen requirements file at `/home/user/automation_project/requirements.txt` using `pip freeze` from the virtual environment. The file must be produced by running `/home/user/automation_project/venv/bin/pip freeze` and redirecting the output to that path.

4. The project script at `/home/user/automation_project/run_workflow.py` imports all three of these packages. Verify the environment works by running the script using the virtual environment's Python interpreter (`/home/user/automation_project/venv/bin/python`) — it should exit with code 0 and print exactly the following line to stdout:

```
Workflow environment OK
```

The final state I care about for testing:
- `/home/user/automation_project/venv/` exists and is a valid Python virtual environment.
- `/home/user/automation_project/requirements.txt` exists and contains lines for `requests`, `schedule`, and `python-dotenv` pinned to the exact versions listed above (the file may contain other dependency lines too, since pip freeze includes transitive deps).
- Running `/home/user/automation_project/venv/bin/python /home/user/automation_project/run_workflow.py` prints `Workflow environment OK` and exits cleanly.

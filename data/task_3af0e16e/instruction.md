I'm a performance engineer setting up a profiling environment for a Python application. I need you to help me get a reproducible environment ready quickly.

Please do the following:

1. Create a Python virtual environment at `/home/user/profiling_env` using the `venv` module.

2. Using the pip inside that virtual environment (i.e., `/home/user/profiling_env/bin/pip`), install these two packages at these exact versions:
   - `pyinstrument==4.6.1`
   - `memory-profiler==0.61.0`

3. After installing, run `pip freeze` using the virtual environment's pip and write the output to `/home/user/profiling_env/requirements.txt`.

The `requirements.txt` file must contain the frozen output of all installed packages (including transitive dependencies). The file must be a plain text file with one `package==version` line per package, exactly as `pip freeze` produces it. The lines must be sorted alphabetically (which is how `pip freeze` outputs them by default).

The two packages I specifically need to be present in `requirements.txt` (among others) are:
- `memory-profiler==0.61.0`
- `pyinstrument==4.6.1`

I'll be verifying that those two exact lines appear in the file and that the file lives at `/home/user/profiling_env/requirements.txt`.

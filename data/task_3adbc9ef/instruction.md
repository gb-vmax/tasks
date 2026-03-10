Hey, I need some help with a CI/CD environment variable audit. I'm a platform engineer and we have a `.env` file at `/home/user/pipeline/.env` that gets loaded by our build system. I need you to process it and produce a sanitized summary for our documentation.

Here's the situation: the `.env` file contains a mix of configuration variables. Some are prefixed with `CI_` (our CI/CD-specific vars), and some are general application vars. Some values are secrets (any variable whose name contains the word `SECRET`, `TOKEN`, or `PASSWORD` — case-insensitive) and must be masked in the output.

Please do the following:

1. From `/home/user/pipeline/.env`, extract **only the lines that start with `CI_`** (ignore blank lines, comments, and any non-`CI_` variables).

2. For each extracted `CI_` variable, if the variable name contains `SECRET`, `TOKEN`, or `PASSWORD` (case-insensitive), replace the value with `****`. Otherwise, keep the value as-is.

3. Sort the resulting lines **alphabetically by variable name**.

4. Write the final output to `/home/user/pipeline/ci_audit.txt`. The file should contain one `KEY=VALUE` pair per line, with no trailing spaces, no blank lines, and no comments. The file should end with a newline after the last entry.

For example, if the input had:
```
CI_BUILD_DIR=/workspace/build
CI_API_TOKEN=abc123secret
CI_RETRY_COUNT=3
```

The output would be:
```
CI_API_TOKEN=****
CI_BUILD_DIR=/workspace/build
CI_RETRY_COUNT=3
```

Please create the `/home/user/pipeline/ci_audit.txt` file following these rules exactly.

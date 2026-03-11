Hey, I need your help with a quick config task. I'm a QA engineer setting up a test environment, and I have a main application config file at `/home/user/configs/app.ini`. I need to extract specific values from it and generate a flat environment variable file that our test runner can source directly.

The file `/home/user/configs/app.ini` already exists. Please read it and create a new file at `/home/user/configs/test_env.sh` based on its contents.

Here's exactly what I need:

1. Read the following values from `app.ini`:
   - From the `[database]` section: `host`, `port`, and `name`
   - From the `[server]` section: `timeout` and `debug`
   - From the `[auth]` section: `secret_key`

2. Write `/home/user/configs/test_env.sh` with the following exact format — one `export` statement per line, using the pattern `export TEST_<SECTION>_<KEY>=<value>` where `<SECTION>` is the INI section name in uppercase and `<KEY>` is the key name in uppercase. The lines must appear in this exact order:

```
export TEST_DATABASE_HOST=<value>
export TEST_DATABASE_PORT=<value>
export TEST_DATABASE_NAME=<value>
export TEST_SERVER_TIMEOUT=<value>
export TEST_SERVER_DEBUG=<value>
export TEST_AUTH_SECRET_KEY=<value>
```

The file should contain exactly these 6 lines and nothing else — no comments, no blank lines, no `#!/bin/bash` header.

For example, if the `[database]` section has `host = localhost`, the corresponding line should be:
```
export TEST_DATABASE_HOST=localhost
```

Note that values in the INI file may have spaces around the `=` sign — the exported values should have no surrounding whitespace.

Once you've created the file, also make it executable with permissions `755`.

Can you take care of this for me?

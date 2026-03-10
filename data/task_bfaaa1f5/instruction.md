I'm a security engineer and I need to rotate an API key in our application's configuration file. Here's what I need done:

The application config file is located at `/home/user/app/config.env`. It contains several environment variable definitions, one of which is `API_KEY`. I need to:

1. Generate a new API key by computing the SHA-256 hash of the string `rotate-$(date +%Y-%m-%d)-secret` using `openssl dgst -sha256 -hmac "prod-salt"`, then take only the hex digest portion (the part after the `= ` in openssl's output). This will be the new API key value.

2. Replace the existing `API_KEY=...` line in `/home/user/app/config.env` with the new value, keeping the same `API_KEY=` key name. The line should be in the format `API_KEY=<new_value>` with no spaces, no quotes around the value, and no trailing characters.

3. Append a single line to the audit log at `/home/user/app/rotation_log.txt` recording this rotation event. The line must be in exactly this format:
   ```
   ROTATED API_KEY on <YYYY-MM-DD> old=<first_8_chars_of_old_key> new=<first_8_chars_of_new_key>
   ```
   Where `<YYYY-MM-DD>` is today's date from `date +%Y-%m-%d`, `<first_8_chars_of_old_key>` is the first 8 characters of the old `API_KEY` value that was in the file before rotation, and `<first_8_chars_of_new_key>` is the first 8 characters of the newly generated key.

The file `/home/user/app/config.env` must remain valid after the operation — all other lines must be unchanged. The audit log at `/home/user/app/rotation_log.txt` already has existing entries and your new line must be appended (not overwrite the file).

Can you perform this credential rotation in the terminal for me?

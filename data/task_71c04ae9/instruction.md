I'm a security engineer and we just had a credential rotation. Our old API key `sk-OLDKEY-v1-abc123def456` has been revoked and needs to be replaced with the new key `sk-NEWKEY-v2-xyz789uvw012` across our deployment configs. The configs are scattered across `/home/user/deployments/` in various subdirectories.

I need you to do the following:

1. Find all `.conf` files under `/home/user/deployments/` (search recursively) that contain the old API key string `sk-OLDKEY-v1-abc123def456`.

2. Replace every occurrence of `sk-OLDKEY-v1-abc123def456` with `sk-NEWKEY-v2-xyz789uvw012` in-place across all those matching files. Files that don't contain the old key should remain completely untouched.

3. Write an audit log to `/home/user/rotation_audit.log` listing exactly which files were modified. The file should contain one absolute path per line, sorted alphabetically, with no extra whitespace or blank lines. For example:
```
/home/user/deployments/app/service.conf
/home/user/deployments/db/primary.conf
```

After you're done, every `.conf` file that previously contained the old key should now contain the new key instead, files that never had the old key should be byte-for-byte identical to before, and the audit log should list exactly the files that were changed.

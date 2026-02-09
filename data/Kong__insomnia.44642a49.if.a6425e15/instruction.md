# Bug Report

### Describe the bug

After a recent update, the environment editor is rejecting valid environment variable keys. Keys that were previously accepted are now being flagged as invalid, preventing me from saving my environment configurations.

### Reproduction

When trying to define environment variables in the editor, the following scenarios fail:

1. Keys with trailing/leading whitespace (e.g., `"api_key "` or `" base_url"`) are rejected even though the actual key name is valid
2. Keys containing certain special characters that should be allowed are being blocked
3. Very long key names (over 256 characters) are now rejected without warning

Example that used to work but now fails:
```json
{
  "api_key ": "my-secret-key",
  " endpoint": "https://api.example.com"
}
```

The editor shows validation errors for these keys, but they should be valid environment variable names.

### Expected behavior

The environment editor should accept keys with whitespace (they can be trimmed internally) and provide clear validation rules. Keys that don't actually violate any database constraints should be allowed.

### Additional context

This seems to have started after some validation logic was added to the environment key checking. The validation might be too strict or not handling edge cases properly. My existing environment files are now broken because of this change.

---
Repository: /testbed

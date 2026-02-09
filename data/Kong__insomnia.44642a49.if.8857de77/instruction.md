# Bug Report

### Describe the bug

When importing cURL commands that contain variables prefixed with `$`, the dollar sign is now being included in the parsed variable name instead of being stripped out. This causes the imported request to use incorrect variable references.

### Reproduction

Try importing a cURL command that uses a variable:

```bash
curl -X GET "$API_URL/users" -H "Authorization: Bearer $TOKEN"
```

After import, the variables appear as `$API_URL` and `$TOKEN` in the request instead of `API_URL` and `TOKEN`. This breaks variable substitution since the variable names now include the `$` prefix.

### Expected behavior

The `$` prefix should be removed from variable names during import, so that:
- `$API_URL` becomes `API_URL`
- `$TOKEN` becomes `TOKEN`

This was working correctly before and the variables were being properly stripped of their `$` prefix.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

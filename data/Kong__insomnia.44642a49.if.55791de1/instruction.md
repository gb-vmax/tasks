# Bug Report

### Describe the bug

When importing cURL commands that contain environment variables (prefixed with `$`), the variable names are being incorrectly parsed. The `$` symbol is included in the parsed variable name instead of being stripped out.

### Reproduction

Try importing a cURL command with an environment variable:

```bash
curl -X GET $API_URL/users
```

After import, the variable name includes the `$` prefix (e.g., `$API_URL`) instead of just the variable name (`API_URL`).

### Expected behavior

Environment variables in cURL commands should have the `$` prefix removed during parsing, so that `$API_URL` becomes `API_URL` in the imported request.

### Additional context

This appears to affect any cURL command containing shell variables. The variable substitution doesn't work correctly because the variable names retain the `$` character.

---
Repository: /testbed

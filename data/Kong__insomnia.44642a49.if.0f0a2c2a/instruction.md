# Bug Report

### Describe the bug

When importing cURL commands that contain variables (strings starting with `$`), the variable names are being incorrectly processed. The `$` character is included in the imported variable name instead of being stripped out properly.

### Reproduction

Try importing a cURL command that uses shell variables:

```bash
curl -X POST $API_URL/endpoint -H "Authorization: Bearer $TOKEN"
```

After import, the variables appear as `$API_URL` and `$TOKEN` in the request instead of `API_URL` and `TOKEN`.

### Expected behavior

The `$` prefix should be removed from variable names during import, so `$API_URL` becomes `API_URL` and `$TOKEN` becomes `TOKEN`.

### Additional context

This seems to have started happening recently. Previously, the dollar sign was correctly stripped from variable names during the cURL import process.

---
Repository: /testbed

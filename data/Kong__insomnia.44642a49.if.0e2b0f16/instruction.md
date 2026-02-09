# Bug Report

### Describe the bug

When importing cURL commands that contain environment variables (starting with `$`), the variable names are being incorrectly processed. The dollar sign is not being removed properly, and in some cases the entire variable reference gets mangled.

### Reproduction

Try importing a cURL command with an environment variable:

```bash
curl -X GET "$API_URL/users" -H "Authorization: Bearer $TOKEN"
```

After import, the variables appear malformed in the request. Instead of removing just the `$` prefix, the entire variable name gets corrupted.

### Expected behavior

Environment variables in cURL commands should have the `$` prefix stripped cleanly, so `$API_URL` becomes `API_URL` and `$TOKEN` becomes `TOKEN`. The variable names should remain intact and usable in the imported request.

### Additional context

This seems to affect any cURL command with dollar sign variables. The issue appears to be in how the importer processes string tokens that contain the `$` character.

---
Repository: /testbed

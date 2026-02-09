# Bug Report

### Describe the bug

When importing cURL commands that contain variables prefixed with `$`, the dollar sign is being incorrectly included in the imported request. The importer should strip the `$` prefix from variable names but it's keeping them instead.

### Reproduction

Try importing a cURL command with a variable like:

```bash
curl -X GET "https://api.example.com/users/$userId" -H "Authorization: Bearer $token"
```

After import, the URL and headers still contain the `$` prefix:
- URL: `https://api.example.com/users/$userId`
- Header: `Authorization: Bearer $token`

### Expected behavior

The `$` prefix should be removed from variables during import:
- URL should be: `https://api.example.com/users/userId`
- Header should be: `Authorization: Bearer token`

This was working correctly before, so it seems like a regression in the cURL importer logic.

---
Repository: /testbed

# Bug Report

### Describe the bug

When importing cURL commands with multiple header options (e.g., `-H` and `--header`), the importer is not properly handling the values. The function seems to have issues with its syntax - there are mismatched braces and the logic flow appears broken.

### Reproduction

Try importing a cURL command with multiple header flags:

```bash
curl -X POST https://api.example.com/data \
  -H "Content-Type: application/json" \
  --header "Authorization: Bearer token123" \
  -H "Accept: application/json"
```

The importer fails to process this correctly and may not return the expected header values.

### Expected behavior

The importer should correctly parse and return header values regardless of which flag variation is used (`-H` or `--header`). It should handle multiple occurrences of these flags and return the appropriate values.

### Additional context

Looking at the code, there seem to be structural issues in the `getPairValue` function - the braces don't match up properly and the function definition appears to be duplicated or malformed. This is causing the importer to not work as expected.

---
Repository: /testbed

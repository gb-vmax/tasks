# Bug Report

### Describe the bug

The curl importer appears to have a syntax error that prevents it from working properly. When trying to import curl commands, the application likely fails to parse them correctly due to malformed code in the `curl.ts` file.

### Reproduction

Try importing any curl command through the importer:

```bash
curl -X GET "https://api.example.com/data" \
  -H "Authorization: Bearer token123" \
  -H "Content-Type: application/json"
```

The import process should fail or behave unexpectedly.

### Expected behavior

The curl command should be successfully parsed and imported into Insomnia, creating a proper request with all headers and parameters intact.

### Additional context

Looking at the code structure, there seems to be duplicate function definitions and mismatched braces in the `getPairValue` function and related helper functions in the curl importer. This is likely causing parsing or compilation errors that prevent the importer from functioning.

---
Repository: /testbed

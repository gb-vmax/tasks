# Bug Report

### Describe the bug

After a recent update, the curl importer seems to have broken syntax. When trying to import curl commands, the application fails to parse them correctly and may crash or behave unexpectedly.

### Reproduction

Try importing any curl command using the curl importer. For example:

```bash
curl -X POST https://api.example.com/data \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

The importer should process this command but instead encounters errors during the parsing phase.

### Expected behavior

The curl command should be imported successfully and converted into a proper request format with all headers and body data preserved.

### Additional context

This appears to be related to the `getPairValue` function in the curl importer. The code seems to have malformed syntax with duplicate function declarations or improperly nested code blocks. The function definition appears to be duplicated or incorrectly structured, which would prevent the importer from working at all.

---
Repository: /testbed

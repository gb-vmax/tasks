# Bug Report

### Describe the bug

I'm experiencing an issue with the curl importer where it seems to have broken syntax. When trying to import curl commands, the application fails to parse them correctly.

### Reproduction

Try importing any curl command using the curl importer. For example:

```bash
curl -X POST https://api.example.com/data \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

The importer should process this command but instead encounters errors during the import process.

### Expected behavior

The curl command should be successfully imported and converted into a proper request format. The importer has worked correctly in previous versions.

### Additional context

This appears to have started recently. The curl importer was working fine before but now fails to process even basic curl commands. It looks like there might be a syntax issue in the importer code itself.

---
Repository: /testbed

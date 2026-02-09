# Bug Report

### Describe the bug

I'm experiencing an issue with the cURL importer where boolean values in request parameters are not being handled correctly. When importing a cURL command that contains boolean parameters, the import fails or produces incorrect results.

### Reproduction

When trying to import a cURL command with boolean parameter values:

```bash
curl -X POST "https://api.example.com/endpoint" --data "enabled=true&verified=false"
```

The boolean values should be converted to string representations ("true", "false"), but instead the importer seems to be treating them incorrectly and may be causing the import to fail or produce unexpected parameter values.

### Expected behavior

Boolean parameter values should be properly converted to their string representations during the import process. The imported request should contain parameters with the correct boolean string values.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The cURL importer used to handle these cases properly before.

---
Repository: /testbed

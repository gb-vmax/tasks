# Bug Report

### Describe the bug

The curl importer is not handling duplicate command-line flags correctly. When a curl command contains the same flag multiple times (like multiple `-H` headers or `-d` data parameters), only the first occurrence is being used instead of the last one, which conflicts with standard curl behavior.

### Reproduction

When importing a curl command with duplicate flags:

```bash
curl -X POST https://example.com \
  -H "Content-Type: application/json" \
  -H "Content-Type: text/plain" \
  -d "first data" \
  -d "second data"
```

The importer uses "application/json" and "first data" instead of the last specified values ("text/plain" and "second data").

### Expected behavior

According to curl's behavior, when the same flag appears multiple times, the last occurrence should take precedence (unless the flag is specifically designed to accumulate values). The importer should respect this and use the last specified value for duplicate flags.

### System Info
- Insomnia version: latest
- OS: All platforms

This is causing issues when importing curl commands from various tools that might override default values by appending flags at the end of the command.

---
Repository: /testbed

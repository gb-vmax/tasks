# Bug Report

### Describe the bug

When importing cURL commands with duplicate flags/options, only the first occurrence is being used instead of the last one. According to cURL's behavior, when the same flag is specified multiple times, the last value should take precedence.

### Reproduction

Try importing a cURL command with duplicate flags:

```bash
curl -X GET -X POST https://example.com
```

Currently, this results in the method being set to `GET`, but it should be `POST` (the last specified value).

Similarly with other duplicate options:
```bash
curl --user alice:pass1 --user bob:pass2 https://example.com
```

The credentials are being set to `alice:pass1` instead of `bob:pass2`.

### Expected behavior

When duplicate flags are present in a cURL command, the importer should respect cURL's standard behavior where the last occurrence of a flag takes precedence over earlier ones. This is how the actual cURL command-line tool handles duplicate options.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed

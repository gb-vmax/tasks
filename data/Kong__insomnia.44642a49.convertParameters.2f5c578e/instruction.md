# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications, required parameters are being set as disabled instead of enabled. This is causing issues where required parameters in the imported requests are not being sent by default, which is the opposite of what should happen.

### Reproduction

1. Create an OpenAPI 3 spec with a required parameter:
```yaml
parameters:
  - name: apiKey
    in: query
    required: true
    schema:
      type: string
```

2. Import the spec into Insomnia
3. Check the imported request

### Expected behavior

Required parameters should be **enabled** by default (not disabled), so they are included in the request. Optional parameters (required: false or not specified) should be disabled by default.

Currently, the behavior is inverted - required parameters are disabled and optional ones are enabled.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed

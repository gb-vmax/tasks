# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, parameters are being set up incorrectly. Required parameters are showing as disabled instead of enabled, and the parameter values aren't being generated from the schema anymore.

### Reproduction

1. Import an OpenAPI 3.0 spec with parameters that have `required: true`
2. Check the imported request parameters
3. Notice that required parameters are disabled (grayed out)
4. Also notice that parameter values are just showing the parameter name instead of example values from the schema

Example OpenAPI spec:
```yaml
parameters:
  - name: userId
    in: path
    required: true
    schema:
      type: string
      example: "12345"
```

### Expected behavior

- Required parameters should be **enabled** by default (not disabled)
- Parameter values should be generated from the schema examples (e.g., "12345" in the example above)
- Optional parameters (required: false or not set) should be disabled

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might be a regression - the logic for handling required parameters appears to be inverted.

---
Repository: /testbed

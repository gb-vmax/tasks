# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, the required parameters are being disabled and optional parameters are being enabled, which is the opposite of what should happen. Additionally, required parameters are not getting their example values generated.

### Reproduction

1. Import an OpenAPI 3.0 specification with the following parameter definition:
```yaml
parameters:
  - name: userId
    in: path
    required: true
    schema:
      type: string
      example: "12345"
  - name: filter
    in: query
    required: false
    schema:
      type: string
      example: "active"
```

2. Check the imported request parameters

### Expected behavior

- Required parameters (`userId`) should be **enabled** by default with their example value populated (`12345`)
- Optional parameters (`filter`) should be **disabled** by default with their example value populated (`active`)

### Actual behavior

- Required parameters are **disabled** and have no value
- Optional parameters are **enabled** with example values

This makes it confusing to work with imported specs since you have to manually enable all required parameters before making requests.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed

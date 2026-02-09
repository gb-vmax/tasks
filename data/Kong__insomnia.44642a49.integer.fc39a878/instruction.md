# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with integer parameters, the generated example values are showing up as `NaN` instead of valid integer values like `0`. This makes the imported requests unusable without manual editing.

### Reproduction

1. Import a Swagger 2.0 spec that contains integer parameters (e.g., path parameters, query parameters with type `integer`)
2. Check the generated example values for those parameters
3. The parameter values are set to `NaN` instead of a valid integer

Example Swagger spec that reproduces the issue:
```yaml
swagger: '2.0'
paths:
  /users/{userId}:
    get:
      parameters:
        - name: userId
          in: path
          type: integer
          required: true
```

### Expected behavior

Integer parameters should have valid example values (like `0`) that can be used directly in requests. Currently getting `NaN` which causes requests to fail.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed

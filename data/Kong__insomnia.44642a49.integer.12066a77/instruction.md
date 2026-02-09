# Bug Report

### Describe the bug
When importing OpenAPI 3 specs with integer parameters, the generated example values are showing up as `undefined` instead of actual integer values. This makes the imported requests less useful since parameters don't have valid example data.

### Reproduction
1. Import an OpenAPI 3 spec that contains integer parameters (e.g., query parameters with `type: integer`)
2. Check the generated request
3. The parameter example value is `undefined` instead of an integer like `0`

Example OpenAPI spec snippet that triggers this:
```yaml
parameters:
  - name: limit
    in: query
    schema:
      type: integer
```

### Expected behavior
Integer parameters should have a valid integer example value (like `0`) generated automatically during import, similar to how other types get default examples.

### System Info
- Insomnia version: latest
- Import format: OpenAPI 3.x

---
Repository: /testbed

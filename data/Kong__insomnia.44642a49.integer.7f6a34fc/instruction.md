# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, integer parameters are being generated with `null` values instead of valid integer examples. This causes issues when trying to use the imported requests, as the API expects actual integer values but receives null instead.

### Reproduction

1. Import a Swagger 2.0 spec that contains integer parameters (e.g., path parameters, query parameters)
2. Check the generated request examples
3. Integer parameters will have `null` as their value instead of a valid integer like `0`

Example Swagger spec snippet that triggers this:
```yaml
parameters:
  - name: userId
    in: path
    type: integer
    required: true
  - name: limit
    in: query
    type: integer
```

### Expected behavior

Integer parameters should be populated with a valid integer example value (like `0`) so that the imported requests can be tested immediately without manual modification. Other numeric types like `number`, `number_float`, and `number_double` correctly generate `0` or `0.0` as examples.

### Actual behavior

Integer parameters are set to `null`, which may cause validation errors or unexpected behavior when sending requests to APIs that expect integer values.

---
Repository: /testbed

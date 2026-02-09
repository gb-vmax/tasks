# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, parameters marked as deprecated are not being properly disabled in the generated requests. According to the OpenAPI spec, deprecated parameters should be disabled by default, but currently they remain enabled if they're marked as required.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: oldParam
          in: query
          required: true
          deprecated: true
          schema:
            type: string
```

When importing this spec:
1. The parameter `oldParam` is marked as both `required: true` and `deprecated: true`
2. After import, the parameter appears as enabled in Insomnia
3. Expected: The parameter should be disabled since it's deprecated

### Expected behavior

Deprecated parameters should be disabled in the imported requests, regardless of their `required` status. This helps developers avoid using deprecated API features.

Additionally, it would be helpful if deprecated parameters had some visual indication (like a `[DEPRECATED]` prefix in the description) to make it clear they shouldn't be used.

### Additional context

Some API specs also use `x-deprecated` as a custom extension field, which should also be recognized as marking a parameter as deprecated.

---
Repository: /testbed

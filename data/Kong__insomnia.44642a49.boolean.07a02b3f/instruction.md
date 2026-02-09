# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications, boolean parameters are no longer generating consistent example values. The generated examples now appear to be random, which makes it difficult to have predictable and reproducible API documentation/testing workflows.

### Reproduction

1. Import an OpenAPI 3 spec with a boolean parameter
2. Generate example values for the parameter multiple times
3. Observe that the boolean value changes randomly between imports

Example OpenAPI spec snippet:
```yaml
parameters:
  - name: isActive
    in: query
    schema:
      type: boolean
```

Previously, this would consistently generate `true` as the example value. Now it randomly generates either `true` or `false`.

### Expected behavior

Boolean parameters should generate consistent, deterministic example values (like they did before). When importing the same spec multiple times, the generated examples should be identical. This is important for:
- Reproducible test cases
- Consistent documentation generation
- Predictable API client generation

### Additional context

This seems to have started happening recently. Other parameter types (string, integer, etc.) still generate consistent examples, only booleans are affected.

---
Repository: /testbed

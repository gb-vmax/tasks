# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications, the parameter descriptions and deprecated flags are being lost. The imported requests don't include any description text for parameters, and there's no indication when a parameter has been marked as deprecated in the OpenAPI spec.

### Reproduction

Given an OpenAPI 3 spec with parameters like:

```yaml
parameters:
  - name: userId
    in: query
    description: The ID of the user to retrieve
    required: true
    schema:
      type: string
  - name: oldParam
    in: query
    description: Legacy parameter for backward compatibility
    deprecated: true
    required: false
    schema:
      type: string
```

After importing this spec into Insomnia:
1. The `userId` parameter appears without its description "The ID of the user to retrieve"
2. The `oldParam` parameter appears without any indication that it's deprecated
3. Both parameters are missing their description metadata

### Expected behavior

- Parameter descriptions from the OpenAPI spec should be preserved in the imported request
- Deprecated parameters should be clearly marked (e.g., with a "[DEPRECATED]" prefix or similar indicator)
- The description field should combine both the deprecation status and the original description

### System Info
- Insomnia version: Latest
- Import format: OpenAPI 3.x

---
Repository: /testbed

# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, deprecated parameters are being automatically disabled in the generated requests. This makes it impossible to test or use deprecated API parameters even though they're still functional in the actual API.

### Reproduction

Given an OpenAPI 3 spec with a deprecated parameter:

```yaml
parameters:
  - name: legacy_filter
    in: query
    deprecated: true
    required: false
    schema:
      type: string
```

When importing this spec into Insomnia, the `legacy_filter` parameter is automatically disabled in the request, even though it's still a valid parameter that the API accepts.

### Expected behavior

Deprecated parameters should be imported as enabled by default (unless they're explicitly not required). The deprecation status could be indicated in the description or with a visual marker, but the parameter should remain functional and enabled so users can still interact with deprecated but working API endpoints.

### Additional context

This is particularly problematic when working with APIs that are in transition - deprecated parameters often still work for backwards compatibility, and developers need to be able to test both old and new parameter versions.

---
Repository: /testbed

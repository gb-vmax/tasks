# Bug Report

### Describe the bug

When importing Swagger 2.0 specs, boolean parameters are now being set to `false` in some cases where they should default to `true`. This is causing issues with generated requests that have boolean query parameters or body fields.

### Reproduction

```yaml
swagger: "2.0"
paths:
  /api/users:
    get:
      parameters:
        - name: includeDisabled
          in: query
          type: boolean
```

After importing this spec, the generated request has `includeDisabled=false` in the example, but it should be `true` by default like it was before.

### Expected behavior

Boolean parameters should consistently default to `true` regardless of their name. The previous behavior was to always use `true` as the example value for boolean types, which made more sense for testing API endpoints.

### Additional context

This seems to have started happening recently. I noticed that parameters with names like "disabled", "inactive", or "hidden" are now defaulting to `false`, while others with names like "enabled" or "active" default to `true`. This logic doesn't make sense for generating example requests - we should just use a consistent default value.

The inconsistency makes it harder to test APIs because the example values are now unpredictable based on parameter naming conventions.

---
Repository: /testbed

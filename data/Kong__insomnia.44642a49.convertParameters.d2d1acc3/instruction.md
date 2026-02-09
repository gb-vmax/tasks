# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with deprecated parameters, the parameters are being marked as disabled in the imported requests. This makes it impossible to test deprecated endpoints that still need to be functional during deprecation periods.

### Reproduction

Given an OpenAPI 3 spec with a deprecated parameter:

```yaml
parameters:
  - name: legacy_field
    in: query
    deprecated: true
    required: true
    schema:
      type: string
```

When importing this spec into Insomnia, the `legacy_field` parameter shows up as disabled in the request, even though it's marked as required. This prevents sending requests to endpoints that still accept (or require) deprecated parameters.

### Expected behavior

Deprecated parameters should be imported with their deprecation status visible (e.g., in the description), but they should not be automatically disabled. The `disabled` field should only be set based on whether the parameter is required or not, regardless of deprecation status.

A deprecated but required parameter should be enabled by default so that requests can still be sent successfully.

### System Info
- Insomnia version: latest
- OpenAPI version: 3.x

---
Repository: /testbed

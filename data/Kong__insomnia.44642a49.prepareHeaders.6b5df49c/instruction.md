# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications, duplicate headers with different casing (e.g., `Accept` and `accept`) are being added to requests. This causes issues with some servers that are strict about header handling or results in redundant headers being sent.

### Reproduction

Given an OpenAPI spec where:
1. A parameter defines a header (e.g., `Accept`)
2. The importer automatically generates an `Accept` header based on response content types
3. Both headers end up in the final request, even though they're the same header with different casing

Example scenario:
```yaml
parameters:
  - name: accept
    in: header
    schema:
      type: string
responses:
  '200':
    content:
      application/json:
        schema:
          type: object
```

After import, the request contains both `accept` and `Accept` headers.

### Expected behavior

Headers should be deduplicated in a case-insensitive manner. HTTP header names are case-insensitive per RFC 7230, so `Accept`, `accept`, and `ACCEPT` should all be treated as the same header. Only one version should appear in the imported request.

### Additional context

This seems to affect the OpenAPI 3 importer specifically. The issue becomes more apparent when specs define headers with non-standard casing or when the auto-generated headers conflict with explicitly defined parameter headers.

---
Repository: /testbed

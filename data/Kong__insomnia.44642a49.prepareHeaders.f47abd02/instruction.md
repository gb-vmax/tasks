# Bug Report

### Describe the bug

I'm encountering an issue with OpenAPI 3.0 import where headers are not being handled correctly. When importing an OpenAPI spec with header parameters defined, the headers aren't appearing in the imported requests. Additionally, the Content-Type header is being added even when it's already explicitly defined in the spec.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /api/users:
    get:
      parameters:
        - name: Authorization
          in: header
          required: true
          schema:
            type: string
        - name: X-Custom-Header
          in: header
          schema:
            type: string
```

When importing this spec:
1. The Authorization and X-Custom-Header parameters don't show up as headers in the request
2. If a Content-Type is already defined in the parameters, it gets duplicated

### Expected behavior

- Header parameters from the OpenAPI spec should be imported and available in the request headers
- Content-Type header should only be added automatically when it's not already defined in the spec

This seems to have broken recently, as previous imports were working fine.

---
Repository: /testbed

# Bug Report

### Describe the bug
When importing OpenAPI 3 specs, header parameters are being excluded instead of included in the generated requests. The importer appears to be filtering out header parameters rather than filtering them in.

### Reproduction
```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
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

When importing this spec, the headers defined in the parameters are not being added to the request. Only non-header parameters seem to be processed.

### Expected behavior
Header parameters defined in the OpenAPI spec should be included in the imported request configuration. The `Authorization` and `X-Custom-Header` headers should be present in the request.

### Additional context
This seems to have broken recently. Previously, header parameters were being imported correctly from OpenAPI 3 specifications. Now they're completely missing from the generated requests.

---
Repository: /testbed

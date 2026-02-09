# Bug Report

### Describe the bug

I'm experiencing an issue with the OpenAPI 3 importer where Content-Type headers are being added incorrectly to requests. It seems like the header is now being added even when it shouldn't be, or in cases where there's no request body.

### Reproduction

When importing an OpenAPI 3 spec:

1. Import a spec with an endpoint that has no request body
2. The imported request includes a Content-Type header even though there's no body
3. Also happens when importing endpoints that already have a Content-Type header defined in parameters

Example spec snippet:
```yaml
paths:
  /users:
    get:
      parameters:
        - name: Authorization
          in: header
          schema:
            type: string
```

After import, the request has an unexpected Content-Type header added.

### Expected behavior

- Content-Type header should only be added when there's an actual request body
- Content-Type header should not be added if one is already defined in the parameters
- GET requests without bodies shouldn't have Content-Type headers

### Additional context

This seems to have broken recently. Previously the importer was correctly handling these cases and only adding the Content-Type header when appropriate.

---
Repository: /testbed

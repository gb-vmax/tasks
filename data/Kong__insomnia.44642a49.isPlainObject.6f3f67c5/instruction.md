# Bug Report

### Describe the bug

After a recent update, the OpenAPI 3 importer is failing to parse valid OpenAPI specifications. The import process appears to hang or crash when processing certain OpenAPI documents that were previously working fine.

### Reproduction

Try importing an OpenAPI 3.x specification file with nested objects and extensions. The importer seems to get stuck during the parsing phase.

Example spec structure that causes issues:
```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
```

### Expected behavior

The OpenAPI spec should import successfully like it did before. The importer should handle nested objects and standard OpenAPI structures without any issues.

### Additional context

This seems to have started happening recently. The same spec files that worked before are now failing to import. Not sure what changed but it's blocking our workflow.

---
Repository: /testbed

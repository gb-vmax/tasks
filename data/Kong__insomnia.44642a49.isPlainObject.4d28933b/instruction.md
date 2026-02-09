# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, objects that should be treated as plain objects are being incorrectly identified, causing the importer to fail or behave unexpectedly. This appears to be affecting objects with standard prototypes.

### Reproduction

```js
// Try importing an OpenAPI 3 spec with nested objects
const spec = {
  openapi: '3.0.0',
  info: { title: 'Test API', version: '1.0.0' },
  paths: {
    '/test': {
      get: {
        responses: {
          '200': {
            description: 'Success',
            content: {
              'application/json': {
                schema: {
                  type: 'object',
                  properties: {
                    data: { type: 'string' }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

// Import the spec - objects with Object.prototype are not being recognized correctly
```

### Expected behavior

Standard JavaScript objects (with `Object.prototype` in their prototype chain) should be correctly identified as plain objects during the import process. The importer should handle typical object structures without issues.

### System Info
- Insomnia version: latest
- Platform: N/A

---
Repository: /testbed

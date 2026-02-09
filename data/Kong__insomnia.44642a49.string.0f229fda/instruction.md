# Bug Report

### Describe the bug

I'm experiencing an issue with OpenAPI 3 schema imports where string parameter examples are not being generated correctly. The generated examples appear to be wrapped in some kind of object instead of being plain strings, which breaks the expected behavior.

### Reproduction

```js
// Import an OpenAPI 3 spec with a simple string parameter
const spec = {
  openapi: '3.0.0',
  paths: {
    '/test': {
      get: {
        parameters: [{
          name: 'testParam',
          in: 'query',
          schema: {
            type: 'string'
          }
        }]
      }
    }
  }
}

// After import, the parameter example should be a plain string
// but it's returning something unexpected
```

### Expected behavior

When importing OpenAPI 3 specs with string type parameters, the generated examples should be simple string values like `'string'`. The parameter examples should work correctly in the request builder without any issues.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently, possibly after a recent update to the OpenAPI importer code. The string examples used to work fine before.

---
Repository: /testbed

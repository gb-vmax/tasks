# Bug Report

### Describe the bug

After a recent update, the OpenAPI spec parser is not working correctly. When loading API specs with component references, the application fails to parse the spec properly and seems to get stuck or produce incorrect output.

### Reproduction

```js
const spec = {
  components: {
    schemas: {
      User: {
        type: 'object',
        properties: {
          name: { type: 'string' }
        }
      }
    }
  },
  paths: {
    '/users': {
      get: {
        responses: {
          '200': {
            content: {
              'application/json': {
                schema: {
                  $ref: '#/components/schemas/User'
                }
              }
            }
          }
        }
      }
    }
  }
}

// Trying to resolve component schema refs
const methodInfo = spec.paths['/users'].get
resolveComponentSchemaRefs(spec, methodInfo)
// This doesn't work as expected anymore
```

### Expected behavior

The function should resolve `$ref` references in the OpenAPI spec and return the resolved schema object. Component references like `#/components/schemas/User` should be properly dereferenced.

### Additional context

This appears to have broken after some recent changes to the `api-specs.ts` file. The spec parsing worked fine in previous versions but now seems to have issues with the resolution logic.

---
Repository: /testbed

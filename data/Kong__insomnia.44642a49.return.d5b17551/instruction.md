# Bug Report

### Describe the bug

After a recent update, the API spec schema resolution functionality appears to be completely broken. When trying to resolve component schema references in OpenAPI specs, the application fails to process the schemas correctly and the resolved output is malformed or missing.

### Reproduction

```js
const spec = {
  contents: {
    components: {
      schemas: {
        User: {
          type: 'object',
          properties: {
            name: { type: 'string' }
          }
        }
      }
    }
  }
};

const methodInfo = {
  requestBody: {
    content: {
      'application/json': {
        schema: {
          $ref: '#/components/schemas/User'
        }
      }
    }
  }
};

const resolved = resolveComponentSchemaRefs(spec, methodInfo);
// Expected: schema references to be resolved
// Actual: broken/unexpected output
```

### Expected behavior

The function should properly resolve all `$ref` references in the schema by looking them up in the components/schemas section and return a fully resolved schema object.

### Additional context

This seems to have broken after the latest changes to the schema resolution logic. The function used to work fine for resolving nested schema references in API specifications.

---
Repository: /testbed

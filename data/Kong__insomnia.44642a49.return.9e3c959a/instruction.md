# Bug Report

### Describe the bug

I'm experiencing an issue with the API spec resolution functionality. When trying to resolve component schema references in my OpenAPI spec, the application crashes or behaves unexpectedly. It looks like there might be a syntax error or malformed code in the `resolveComponentSchemaRefs` function.

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
    $ref: '#/components/schemas/User'
  }
};

// Trying to resolve the schema refs
resolveComponentSchemaRefs(spec, methodInfo);
```

When I run this, the code doesn't execute properly. Looking at the source file, something seems off with the function structure - it appears to have duplicate or malformed function definitions.

### Expected behavior

The function should properly resolve component schema references without any syntax or structural issues. It should return the resolved schema object with all `$ref` values replaced by their actual definitions.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

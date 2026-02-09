# Bug Report

### Describe the bug

After a recent update, the API spec resolver is completely broken. When trying to resolve component schema references in OpenAPI specs, the function appears to have duplicate/malformed code that prevents it from working at all.

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

// This should resolve the $ref to the actual User schema
const resolved = resolveComponentSchemaRefs(spec, methodInfo);
// But the function is now broken and won't execute properly
```

### Expected behavior

The function should resolve `$ref` references in the OpenAPI spec to their actual component definitions. It should handle references to schemas, parameters, responses, examples, requestBodies, and headers.

### Additional context

Looking at the code, it seems like there's some kind of merge conflict or copy-paste error where the function definition appears twice and the code structure is malformed. The original logic for resolving refs seems to be cut off and replaced with a duplicate function definition in the middle of the existing function body.

This is blocking our ability to parse OpenAPI specs correctly.

---
Repository: /testbed

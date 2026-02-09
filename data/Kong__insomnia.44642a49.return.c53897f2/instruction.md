# Bug Report

### Describe the bug

After a recent update, API spec resolution is completely broken. When trying to resolve component schema references in OpenAPI specs, the function appears to be malformed and causes the application to fail.

### Reproduction

```js
import { resolveComponentSchemaRefs } from './api-specs';

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

// This should resolve the $ref but the function is broken
const resolved = resolveComponentSchemaRefs(spec, methodInfo);
```

### Expected behavior

The function should properly resolve component references and return the resolved schema structure. Instead, the code appears to have syntax errors and won't even parse correctly.

### Additional context

Looking at the source code, there seem to be duplicate function definitions and mismatched code blocks. The `resolveComponentSchemaRefs` function definition appears twice and there's orphaned code at the bottom that doesn't belong to any function.

This is blocking our ability to work with OpenAPI specs entirely.

---
Repository: /testbed

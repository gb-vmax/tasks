# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2.0 import where string parameters are not being generated correctly. When importing a Swagger 2.0 spec with string type parameters, the example values are showing up as function objects instead of actual string values.

### Reproduction

```js
// Import a Swagger 2.0 spec with a string parameter
const spec = {
  swagger: '2.0',
  paths: {
    '/users': {
      get: {
        parameters: [
          {
            name: 'username',
            in: 'query',
            type: 'string'
          }
        ]
      }
    }
  }
}

// After import, the parameter example is a function instead of 'string'
```

### Expected behavior

String parameters should have the example value `'string'` (or a similar placeholder string), not a function object. Other parameter types like `string_email`, `string_date-time`, etc. work correctly and return proper string values.

### System Info
- Insomnia version: latest
- OS: N/A

This seems to have broken recently as string parameters were working fine before. The generated examples are now unusable in the UI.

---
Repository: /testbed

# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, the importer crashes with a reference error. It appears that `apiDocument` is being accessed but is not defined in the scope where it's being used.

### Reproduction

```js
// Import an OpenAPI 3.0 spec with email parameter format
const spec = {
  openapi: '3.0.0',
  servers: [{ url: 'https://api.mycompany.com' }],
  paths: {
    '/users': {
      post: {
        parameters: [{
          name: 'email',
          in: 'query',
          schema: {
            type: 'string',
            format: 'email'
          }
        }]
      }
    }
  }
};

// Try to import this spec - it will fail
```

### Expected behavior

The OpenAPI 3 spec should import successfully and generate example email addresses for email-formatted string parameters. The importer should be able to extract the domain from the server URL if available.

### Actual behavior

The import fails because `apiDocument` is referenced but not defined in the function scope. This prevents any OpenAPI spec with email format parameters from being imported.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

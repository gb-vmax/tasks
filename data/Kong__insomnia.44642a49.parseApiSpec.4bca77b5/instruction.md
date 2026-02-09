# Bug Report

### Describe the bug

I'm encountering an issue when trying to parse API specifications. The parser seems to hang or fail when processing certain OpenAPI/Swagger specs, particularly when they contain server configuration details.

### Reproduction

```js
const apiSpec = {
  openapi: '3.0.0',
  info: {
    title: 'My API',
    version: '1.0.0'
  },
  paths: {
    '/users': {
      get: {
        summary: 'Get users'
      }
    }
  },
  servers: [
    {
      url: 'https://api.example.com',
      description: 'Production server'
    }
  ]
};

// Parsing fails or produces incomplete results
const parsed = parseApiSpec(JSON.stringify(apiSpec));
```

### Expected behavior

The API spec should be parsed successfully and all metadata including server configurations should be extracted properly. The parser should handle both OpenAPI 3.x and Swagger 2.x formats without issues.

### Additional context

This seems to happen specifically with specs that have server/host configurations. Simpler specs without these fields parse fine. Not sure if this is related to a recent change but it's blocking our workflow.

---
Repository: /testbed

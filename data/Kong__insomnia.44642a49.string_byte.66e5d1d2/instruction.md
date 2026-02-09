# Bug Report

### Describe the bug

After a recent update, the Swagger 2.0 importer is generating invalid syntax when processing parameters with `string_byte` format. The code appears to have malformed function definitions that break the parameter example generation.

### Reproduction

```js
// Import a Swagger 2.0 spec with a byte string parameter
const spec = {
  swagger: '2.0',
  paths: {
    '/test': {
      post: {
        parameters: [{
          name: 'data',
          in: 'body',
          schema: {
            type: 'string',
            format: 'byte',
            minLength: 10
          }
        }]
      }
    }
  }
};

// Try to import this spec
// The importer fails with a syntax error
```

### Expected behavior

The importer should successfully parse Swagger 2.0 specifications with byte string parameters and generate valid base64-encoded example values. Parameters with minLength/maxLength constraints should be respected when generating examples.

### System Info
- Insomnia version: latest
- OS: macOS

The error seems to be related to how the `string_byte` generator function is defined in the swagger-2 importer. There's something wrong with the code structure that's preventing it from working correctly.

---
Repository: /testbed

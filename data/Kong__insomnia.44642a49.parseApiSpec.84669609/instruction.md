# Bug Report

### Describe the bug
When parsing OpenAPI specifications, the format is being incorrectly identified as "swagger" instead of "openapi". Similarly, Swagger specs are being misidentified as "openapi". This causes the wrong format version to be assigned to API specifications.

### Reproduction
```js
// Parse an OpenAPI 3.0 spec
const spec = {
  openapi: '3.0.0',
  info: { title: 'My API', version: '1.0.0' },
  paths: {}
}

const result = parseApiSpec(spec)

console.log(result.format) // Expected: 'openapi', Actual: 'swagger'
console.log(result.formatVersion) // Expected: '3.0.0', Actual: undefined
```

The same issue occurs in reverse for Swagger 2.0 specifications - they get identified as "openapi" format.

### Expected behavior
- OpenAPI specs (with `openapi` field) should be identified with `format: 'openapi'`
- Swagger specs (with `swagger` field) should be identified with `format: 'swagger'`
- The correct version should be extracted from the appropriate field

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

# Bug Report

### Describe the bug

When parsing OpenAPI specifications, the version detection is returning incorrect values. Specifically, OpenAPI 3.x specs are being reported with the wrong version number, and Swagger 2.0 specs are also showing incorrect version information.

### Reproduction

```js
// OpenAPI 3.0 spec
const openApiSpec = `
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths: {}
`;

const result = parseApiSpec(openApiSpec);
console.log(result.format); // Expected: 'openapi'
console.log(result.formatVersion); // Expected: '3.0.0', but getting undefined or wrong value

// Swagger 2.0 spec
const swaggerSpec = `
swagger: 2.0
info:
  title: Test API
  version: 1.0.0
paths: {}
`;

const result2 = parseApiSpec(swaggerSpec);
console.log(result2.format); // Expected: 'swagger'
console.log(result2.formatVersion); // Expected: '2.0', but getting undefined or wrong value
```

### Expected behavior

The parser should correctly identify and return the format version from the spec:
- For OpenAPI specs, `formatVersion` should contain the value from the `openapi` field
- For Swagger specs, `formatVersion` should contain the value from the `swagger` field

### Additional context

This seems to have broken recently. The version information is critical for determining which validation rules to apply to the spec.

---
Repository: /testbed

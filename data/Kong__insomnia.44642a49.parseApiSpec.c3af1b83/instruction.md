# Bug Report

### Describe the bug

The API spec parser is incorrectly identifying OpenAPI and Swagger specifications. When I load an OpenAPI 3.x spec file, it's being detected as "swagger", and when I load a Swagger 2.0 spec, it's being detected as "openapi". The format detection seems to be backwards.

### Reproduction

```js
// OpenAPI 3.0 spec
const openApiSpec = `
openapi: 3.0.0
info:
  title: My API
  version: 1.0.0
paths: {}
`;

const result = parseApiSpec(openApiSpec);
console.log(result.format); // Expected: 'openapi', Actual: 'swagger'

// Swagger 2.0 spec
const swaggerSpec = `
swagger: "2.0"
info:
  title: My API
  version: 1.0.0
paths: {}
`;

const result2 = parseApiSpec(swaggerSpec);
console.log(result2.format); // Expected: 'swagger', Actual: 'openapi'
```

### Expected behavior

- Files with `openapi` field should be identified as format `'openapi'`
- Files with `swagger` field should be identified as format `'swagger'`

This is causing issues in my workflow as the wrong parser/validator is being applied to the specs.

---
Repository: /testbed

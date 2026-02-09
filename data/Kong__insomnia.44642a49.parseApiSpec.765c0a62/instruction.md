# Bug Report

### Describe the bug

The API spec parser is incorrectly identifying OpenAPI and Swagger specifications. When I import an OpenAPI 3.x spec, it's being labeled as "swagger", and when I import a Swagger 2.0 spec, it's being labeled as "openapi". This is causing issues with validation and spec-specific features that depend on the correct format being detected.

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
console.log(result.format); // Expected: "openapi", Actual: "swagger"

// Swagger 2.0 spec
const swaggerSpec = `
swagger: "2.0"
info:
  title: Test API
  version: 1.0.0
paths: {}
`;

const result2 = parseApiSpec(swaggerSpec);
console.log(result2.format); // Expected: "swagger", Actual: "openapi"
```

### Expected behavior

- OpenAPI 3.x specifications (with `openapi` field) should be identified with format "openapi"
- Swagger 2.0 specifications (with `swagger` field) should be identified with format "swagger"

The format detection appears to be reversed from what it should be.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

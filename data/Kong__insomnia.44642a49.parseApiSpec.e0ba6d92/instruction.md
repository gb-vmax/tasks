# Bug Report

### Describe the bug

After a recent update, the API spec parser is throwing errors when parsing valid OpenAPI and Swagger specifications. The parser now rejects specs with version numbers that don't match a very specific format, even though these specs were working fine before.

### Reproduction

```js
const swaggerSpec = `
swagger: "2"
info:
  title: My API
  version: 1.0.0
paths: {}
`;

// This now throws an error: "Invalid Swagger version: 2"
const parsed = parseApiSpec(swaggerSpec);
```

Similarly for OpenAPI:

```js
const openApiSpec = `
openapi: "3"
info:
  title: My API
  version: 1.0.0
paths: {}
`;

// This throws: "Invalid OpenAPI version: 3"
const parsed = parseApiSpec(openApiSpec);
```

### Expected behavior

The parser should accept version numbers like "2" for Swagger and "3" for OpenAPI, not just "2.x" and "3.x" formats. Many valid API specifications use shortened version numbers without the patch version, and these were working previously.

### System Info

- Insomnia version: latest
- OS: macOS

This is blocking our workflow since we have several API specs that use the shorter version format. Would appreciate if this could be looked into!

---
Repository: /testbed

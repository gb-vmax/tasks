# Bug Report

### Describe the bug

After a recent update, API spec parsing is failing silently. When I try to import an OpenAPI or Swagger spec, the format and version are not being detected properly. The spec appears to load but none of the format-specific features work.

### Reproduction

```js
const rawSpec = `
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths: {}
`;

const result = parseApiSpec(rawSpec);
// result.format is null instead of 'openapi'
// result.formatVersion is null instead of '3.0.0'
```

### Expected behavior

The parser should correctly identify the spec format (OpenAPI or Swagger) and extract the version number. When I pass in a valid OpenAPI 3.0 spec, I expect:
- `result.format` to be `'openapi'`
- `result.formatVersion` to be `'3.0.0'`

Same goes for Swagger specs - the format and version should be properly detected.

### Additional context

This seems to have broken recently. Previously imported specs are showing up without their format information, and new imports aren't working either. The app still loads but all the OpenAPI/Swagger specific tooling is unavailable.

---
Repository: /testbed

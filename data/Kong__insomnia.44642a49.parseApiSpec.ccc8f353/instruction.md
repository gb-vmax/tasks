# Bug Report

### Describe the bug

When parsing API spec files, if a spec contains both `openapi` and `swagger` fields, the parser doesn't handle it correctly. The current implementation seems to have issues determining the correct format when both fields are present in the document.

### Reproduction

```js
const specWithBothFields = `
openapi: 3.0.0
swagger: 2.0
info:
  title: Test API
  version: 1.0.0
paths: {}
`;

const result = parseApiSpec(specWithBothFields);
// Expected: Should detect as OpenAPI 3.0.0
// Actual: Format detection may fail or return unexpected results
```

### Expected behavior

The parser should correctly identify the API spec format even when a document contains both `openapi` and `swagger` fields. It should prioritize one format over the other consistently (e.g., if `openapi` field exists, treat it as OpenAPI regardless of whether `swagger` field is also present).

### Additional context

This can happen with malformed or incorrectly migrated spec files where someone might have added an `openapi` field without removing the old `swagger` field. The parser should handle these edge cases gracefully.

---
Repository: /testbed

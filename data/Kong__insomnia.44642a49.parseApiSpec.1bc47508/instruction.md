# Bug Report

### Describe the bug

After a recent update, the `parseApiSpec` function is returning objects with additional properties (`isValid`, `validationErrors`, `metadata`) that weren't part of the original API. This is breaking code that expects the function to only return the documented properties (`contents`, `rawContents`, `format`, `formatVersion`).

### Reproduction

```js
import { parseApiSpec } from './api-specs';

const apiSpecString = `
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      summary: Test endpoint
`;

const result = parseApiSpec(apiSpecString);
console.log(Object.keys(result));
// Expected: ['contents', 'rawContents', 'format', 'formatVersion']
// Actual: ['contents', 'rawContents', 'format', 'formatVersion', 'isValid', 'validationErrors', 'metadata']
```

The function now initializes these extra fields in the result object, but they're never populated or used anywhere in the actual parsing logic. This causes issues when:

1. Code destructures the result expecting only the original 4 properties
2. Serialization/deserialization expects a specific shape
3. Type definitions don't match the runtime object

### Expected behavior

The `parseApiSpec` function should only return the properties defined in the `ParsedApiSpec` interface, which are:
- `contents`
- `rawContents` 
- `format`
- `formatVersion`

Any new properties should either be properly implemented throughout the function or removed from the initial result object.

---
Repository: /testbed

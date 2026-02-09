# Bug Report

### Describe the bug
When using the `data.import.raw()` plugin API, the function now throws an error when trying to import valid content. The import process fails with "Invalid JSON content" even though the content being imported is valid.

### Reproduction
```js
// This used to work but now fails
await context.data.import.raw(`{
  "resources": [
    {
      "_type": "request",
      "name": "Test Request"
    }
  ]
}`);
```

The error thrown is: `Invalid JSON content: Unexpected token...`

### Steps to reproduce:
1. Create a plugin that uses the `data.import.raw()` API
2. Pass valid JSON content with whitespace/formatting
3. The import fails with a JSON parsing error

### Expected behavior
The import should succeed when valid JSON content is provided, regardless of formatting or whitespace. The function should parse and import the resources correctly.

### Additional context
This appears to have started happening recently. The same import content that worked before is now being rejected. The validation logic seems to be too strict or parsing the content incorrectly.

---
Repository: /testbed

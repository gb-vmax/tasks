# Bug Report

### Describe the bug

I'm encountering an issue with the cURL importer when handling boolean values in request parameters. When a parameter contains a boolean value, it's not being properly converted to a string parameter, which causes the import to fail or produce incorrect results.

### Reproduction

```js
// When importing a cURL command with boolean parameters
const pair = true;
const result = pairToParameters(pair);

// Expected: [{ name: '', value: 'true' }]
// Actual: The boolean is not handled correctly
```

This seems to affect cURL imports that contain boolean flags or parameters that get parsed as boolean values instead of strings.

### Expected behavior

Boolean values should be converted to their string representation (`'true'` or `'false'`) and included as parameters in the imported request. The importer should handle boolean pairs the same way it handles other primitive values.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

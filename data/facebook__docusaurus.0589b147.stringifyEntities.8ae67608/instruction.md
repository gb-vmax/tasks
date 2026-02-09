# Bug Report

### Describe the bug

I'm encountering an issue with HTML entity stringification where the output is completely broken. Instead of getting properly escaped HTML entities, I'm getting unexpected results or errors when trying to stringify text content.

### Reproduction

```js
const { stringifyEntities } = require('stringify-entities');

// Try to escape HTML entities
const result = stringifyEntities('Hello & goodbye <world>');
console.log(result);
// Expected: 'Hello &amp; goodbye &lt;world&gt;'
// Actual: [object Object] or TypeError
```

When calling `stringifyEntities` with a string value and optional configuration, the function doesn't produce the expected escaped output. It seems like the arguments are being processed incorrectly.

### Expected behavior

The function should accept a string value as the first argument and an optional options object as the second argument, then return a properly escaped string with HTML entities encoded.

### System Info
- rehype-stringify version: 10.0.0
- Node.js version: Latest

This appears to have broken recently - the entity encoding was working fine before. Any help would be appreciated!

---
Repository: /testbed

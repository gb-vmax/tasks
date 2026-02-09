# Bug Report

### Describe the bug

The `stripNumberPrefix` function is not correctly removing number prefixes from strings. Instead of stripping the prefix, it appears to be duplicating or mangling the filename in an unexpected way.

### Reproduction

```js
import {stripNumberPrefix} from '@docusaurus/plugin-content-docs';

const input = '01-my-document';
const result = stripNumberPrefix(input, defaultParser);

console.log(result);
// Expected: 'my-document'
// Actual: something else entirely
```

This affects sidebar generation and document routing when using numbered prefixes to control ordering.

### Expected behavior

When calling `stripNumberPrefix` on a string like `"01-my-document"`, it should return `"my-document"` with the number prefix removed. The function should cleanly strip any numeric prefix and separator, leaving only the actual filename.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

The `stripNumberPrefix` function is returning the wrong value after processing. Instead of returning just the filename without the number prefix, it's returning the entire parser result object converted to a string.

### Reproduction

```js
import {stripNumberPrefix, DefaultNumberPrefixParser} from '@docusaurus/plugin-content-docs';

const input = '01-my-document.md';
const result = stripNumberPrefix(input, DefaultNumberPrefixParser);

console.log(result);
// Expected: 'my-document.md'
// Actual: '[object Object]' or similar stringified object
```

When using `stripNumberPrefix` with a numbered filename, the function returns a stringified object instead of the cleaned filename string.

### Expected behavior

The function should return only the filename portion with the number prefix removed. For example:
- Input: `'01-my-document.md'` → Output: `'my-document.md'`
- Input: `'5-intro.md'` → Output: `'intro.md'`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

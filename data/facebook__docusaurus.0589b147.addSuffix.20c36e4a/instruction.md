# Bug Report

### Describe the bug

The `addSuffix()` function is not appending the suffix correctly to strings. Instead of adding the suffix at the end of the string, it seems to be doing something unexpected with the string manipulation.

### Reproduction

```js
import { addSuffix } from '@docusaurus/utils';

// Expected: "hello.md"
// Actual: Returns wrong result
const result = addSuffix('hello', '.md');
console.log(result);

// Expected: "path/to/file/"
// Actual: Returns wrong result
const path = addSuffix('path/to/file', '/');
console.log(path);
```

### Expected behavior

When calling `addSuffix(str, suffix)`, the suffix should be appended to the end of the string if it's not already present. For example:
- `addSuffix('hello', '.md')` should return `'hello.md'`
- `addSuffix('hello.md', '.md')` should return `'hello.md'` (no duplicate)
- `addSuffix('path/to/file', '/')` should return `'path/to/file/'`

### System Info

- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

The `addSuffix` utility function is not working as expected. When I try to add a suffix to a string, it's behaving incorrectly - sometimes it doesn't add the suffix when it should, and other times it duplicates the suffix.

### Reproduction

```js
import { addSuffix } from '@docusaurus/utils';

// Expected: "hello.md"
// Actual: "hello"
console.log(addSuffix('hello', '.md'));

// Expected: "test.txt" (should not duplicate)
// Actual: "test.txt.txt"
console.log(addSuffix('test.txt', '.txt'));
```

### Expected behavior

The function should:
1. Add the suffix if it's not already present
2. Return the string unchanged if the suffix is already there (no duplication)

For example:
- `addSuffix('hello', '.md')` should return `'hello.md'`
- `addSuffix('hello.md', '.md')` should return `'hello.md'` (not `'hello.md.md'`)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

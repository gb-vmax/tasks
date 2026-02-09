# Bug Report

### Describe the bug

The `removeSuffix` function is not working as expected. Instead of removing a suffix from the end of a string, it appears to be removing text from the beginning of the string (like a prefix removal).

### Reproduction

```js
import { removeSuffix } from '@docusaurus/utils';

// Expected: "hello"
// Actual: ""
console.log(removeSuffix("hello.md", ".md"));

// Expected: "test"  
// Actual: "test.txt"
console.log(removeSuffix("test.txt", ".txt"));
```

### Expected behavior

`removeSuffix(str, suffix)` should remove the suffix from the **end** of the string if it exists, otherwise return the original string unchanged.

For example:
- `removeSuffix("hello.md", ".md")` should return `"hello"`
- `removeSuffix("test.txt", ".txt")` should return `"test"`
- `removeSuffix("file.js", ".md")` should return `"file.js"` (no change since suffix doesn't match)

### Additional context

Also noticed that when passing an empty string as the suffix, the function returns an empty string instead of the original string, which seems incorrect.

---
Repository: /testbed

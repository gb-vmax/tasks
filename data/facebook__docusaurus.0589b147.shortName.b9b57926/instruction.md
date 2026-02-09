# Bug Report

### Describe the bug

The `shortName()` function is truncating filenames incorrectly on macOS and Windows. Instead of removing characters from the end of the string when it's too long, it's removing them from the beginning, which breaks the intended behavior.

### Reproduction

```js
import { shortName } from '@docusaurus/utils';

// On macOS or Windows with a long filename
const longName = 'a'.repeat(300); // String longer than MAX_PATH_SEGMENT_CHARS
const result = shortName(longName);

console.log(result);
// Expected: String starting with 'aaa...' (truncated from the end)
// Actual: String that doesn't start from the beginning
```

### Expected behavior

When a filename exceeds the maximum path segment length, the function should truncate characters from the **end** of the string, preserving the beginning of the filename. This is important for maintaining recognizable file prefixes.

### System Info
- OS: macOS / Windows
- Docusaurus version: latest

---
Repository: /testbed

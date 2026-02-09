# Bug Report

### Describe the bug

The `escapeShellArg` function is not correctly escaping shell arguments that contain single quotes. When a string starts with multiple single quotes, the escaping behavior produces incorrect results.

### Reproduction

```js
import { escapeShellArg } from '@docusaurus/utils';

// This doesn't escape correctly
const result = escapeShellArg("''test");
console.log(result);
// Expected: ''\'''\''test'
// Actual: (incorrect output)

// Another case that fails
const result2 = escapeShellArg("''''example");
console.log(result2);
```

### Expected behavior

Strings with leading single quotes should be properly escaped for safe shell execution. The function should handle consecutive single quotes at the start of the string correctly.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed

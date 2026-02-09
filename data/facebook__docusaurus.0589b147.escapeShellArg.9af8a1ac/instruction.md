# Bug Report

### Describe the bug

The `escapeShellArg` function is not properly handling consecutive empty quotes at the beginning of shell arguments. When a string starts with multiple single quotes, only the first pair is being removed instead of all consecutive pairs.

### Reproduction

```js
import { escapeShellArg } from '@docusaurus/utils';

// Test with a string that results in leading empty quotes
const input = "'test";
const escaped = escapeShellArg(input);

// The output still contains unwanted empty quotes at the start
console.log(escaped);
// Expected: ''\''test'
// Actual: '''''\''test' (or similar with extra quotes)
```

### Expected behavior

All consecutive empty quote pairs (`''`) at the beginning of the escaped string should be removed, not just the first occurrence. The regex should use the global flag to match all instances at the start of the string.

### System Info
- @docusaurus/utils version: latest
- Node.js version: 18.x

---
Repository: /testbed

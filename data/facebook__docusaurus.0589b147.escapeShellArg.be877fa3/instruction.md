# Bug Report

### Describe the bug

I'm experiencing an issue with the shell argument escaping function. When trying to escape strings that contain single quotes, the output is malformed and produces invalid shell syntax.

### Reproduction

```js
const { escapeShellArg } = require('@docusaurus/utils');

// This produces incorrect output
const result = escapeShellArg("it's a test");
console.log(result);
// Expected: 'it'\''s a test'
// Actual: 'it"\"'"s a test'
```

When I try to use the escaped string in a shell command, it fails to parse correctly because the quotes aren't being escaped properly.

### Expected behavior

The function should escape single quotes in a way that's compatible with shell syntax. Single quotes within the string should be properly escaped so the resulting string can be safely used in shell commands.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed

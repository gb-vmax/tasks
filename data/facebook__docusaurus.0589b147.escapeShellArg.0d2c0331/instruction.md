# Bug Report

### Describe the bug

I'm experiencing an issue with shell argument escaping when dealing with strings that contain single quotes. The escaped output appears to be incorrect and doesn't properly handle the quote characters.

### Reproduction

```js
import { escapeShellArg } from '@docusaurus/utils';

// Test with a string containing single quotes
const input = "it's a test";
const escaped = escapeShellArg(input);
console.log(escaped);

// The output doesn't seem to escape correctly
// Expected: 'it'\''s a test'
// Actual: incorrect escaping behavior
```

When I try to use the escaped string in a shell command, it doesn't work as expected and the quotes aren't being handled properly.

### Expected behavior

The function should correctly escape single quotes in shell arguments so they can be safely used in shell commands. Strings containing single quotes should be properly escaped to prevent shell injection and ensure the argument is parsed correctly.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

The `escapeShellArg` function is not properly escaping shell arguments that contain single quotes. When a string with single quotes is passed to this function, the output has an extra trailing `''` appended, which breaks shell command execution.

### Reproduction

```js
import { escapeShellArg } from '@docusaurus/utils';

const input = "test's value";
const escaped = escapeShellArg(input);
console.log(escaped);
// Output: 'test'\''s value'''
// Expected: 'test'\''s value'

// The extra '' at the end causes issues when used in shell commands
```

Another example:
```js
const simple = "hello";
const escaped = escapeShellArg(simple);
console.log(escaped);
// Output: 'hello'''
// Expected: 'hello'
```

### Expected behavior

The function should escape single quotes correctly without adding extra trailing quotes. Strings without quotes should remain unchanged (wrapped in single quotes), and strings with quotes should have them properly escaped without additional characters.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

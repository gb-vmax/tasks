# Bug Report

### Describe the bug

The `toKebabCase` function is now stripping out numbers from strings, which breaks functionality when converting strings that contain numeric characters to kebab-case format.

### Reproduction

```js
import { toKebabCase } from './misc';

// Numbers are being removed from the output
console.log(toKebabCase('test123')); 
// Expected: 'test123'
// Actual: 'test'

console.log(toKebabCase('my-value-2'));
// Expected: 'my-value-2'
// Actual: 'my-value-'

console.log(toKebabCase('HTTP2Protocol'));
// Expected: 'http2-protocol'
// Actual: 'http-protocol'
```

### Expected behavior

The function should preserve numeric characters in the output string. Numbers are valid characters in kebab-case naming conventions and should not be stripped out.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

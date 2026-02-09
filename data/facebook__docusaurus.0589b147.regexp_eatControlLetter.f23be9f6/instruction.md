# Bug Report

### Describe the bug

I'm encountering a critical issue where regex control letter parsing appears to be completely broken. When trying to use regular expressions with control escape sequences (like `\cA`, `\cZ`, etc.), the parser fails to recognize them properly.

### Reproduction

```js
// Trying to match control characters in regex
const pattern = /\cA/;
const text = String.fromCharCode(1); // Control-A character

// This should match but doesn't work correctly
pattern.test(text);
```

### Expected behavior

Regular expressions with control letter escapes (e.g., `\cA` through `\cZ`) should be parsed correctly and match the corresponding control characters. The control letter value should be computed as `(character code) % 32` to get the proper control character value.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a regression as control letter sequences are a standard part of regex syntax. Any regex pattern using `\c` followed by a letter is now broken.

---
Repository: /testbed

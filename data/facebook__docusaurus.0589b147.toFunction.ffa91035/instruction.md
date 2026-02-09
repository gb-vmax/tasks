# Bug Report

### Describe the bug

I'm experiencing an issue with string replacement functionality in remark-gfm. When passing a string value as the replacement argument, it's not being handled correctly and appears to cause infinite recursion or unexpected behavior.

### Reproduction

```js
// Using a string replacement value
const result = replaceText('hello world', 'world', 'universe');
// Expected: 'hello universe'
// Actual: throws error or hangs

// This used to work fine in previous versions
const text = 'foo bar baz';
const replaced = replaceText(text, 'bar', 'qux');
// Should return 'foo qux baz' but doesn't work as expected
```

### Expected behavior

When providing a string as the replacement value, it should be used directly to replace matched text. The function should handle both string and function replacements correctly without causing errors.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems like a regression from the previous version where string replacements worked without issues. The replacement logic appears to have changed in a way that breaks the string use case.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with shell argument escaping where leading single quotes are not being properly handled. When a string starts with single quotes, the escaped output is incorrect and doesn't preserve the original quotes as expected.

### Reproduction

```js
const escaped = escapeShellArg("'test");
// Current output: test'
// Expected output: \'test'
```

The function seems to be stripping leading quotes entirely instead of escaping them properly. This breaks shell commands that need to include literal single quotes at the beginning of arguments.

### Expected behavior

Leading single quotes should be escaped (converted to `\'`) rather than being removed from the output. The escaped string should preserve all quote characters from the original input.

### Additional context

This affects any use case where shell arguments might legitimately start with quote characters, such as passing quoted strings or special characters to shell commands.

---
Repository: /testbed

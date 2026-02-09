# Bug Report

### Describe the bug

I'm experiencing an issue with character code validation in the remark-directive parser. When processing certain Unicode characters, the parser is throwing errors because it's trying to pass numeric character codes directly to `regex.test()` instead of converting them to strings first.

### Reproduction

```js
// This should work but throws an error
const code = 32; // space character
regexCheck(/\s/)(code);

// Error: regex.test expects a string but receives a number
```

The problem occurs when the parser encounters valid character codes that need to be tested against regex patterns. The regex test method expects a string input, but it's receiving raw numeric character codes.

### Expected behavior

Character codes should be properly converted to their string representation using `String.fromCharCode()` before being tested against the regex pattern. This would allow proper validation of whitespace and other Unicode characters.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

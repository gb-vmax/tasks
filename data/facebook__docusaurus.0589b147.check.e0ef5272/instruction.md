# Bug Report

### Describe the bug
I'm encountering an issue with character code validation in the markdown parser. When processing certain Unicode characters, the parser appears to be checking the wrong character code, causing valid whitespace characters to be incorrectly rejected or invalid characters to be accepted.

### Reproduction
```js
// Processing text with Unicode whitespace characters
const text = "Hello\u0020World";  // U+0020 is a regular space

// The parser fails to recognize valid whitespace
// Expected: space character should be detected
// Actual: space character is not properly validated
```

When parsing markdown content with various Unicode whitespace characters, the validation logic seems off by one. Characters that should pass validation are failing, and vice versa.

### Expected behavior
The regex check should correctly validate character codes against the Unicode whitespace pattern. Valid whitespace characters (like U+0020, U+0009, etc.) should be properly recognized, and the character code comparison should work as intended.

### System Info
- Using remark-directive 3.0.0
- Issue appears to be in the regexCheck function

---
Repository: /testbed

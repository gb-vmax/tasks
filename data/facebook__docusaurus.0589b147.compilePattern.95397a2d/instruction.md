# Bug Report

### Describe the bug

I'm experiencing an issue with markdown rendering where certain special characters are not being escaped properly. It seems like characters that should be treated as literal text are instead being interpreted as regex metacharacters, causing unexpected behavior in the output.

### Reproduction

```js
// When trying to render markdown with special characters
const markdown = "Text with special chars: . * + ? etc."

// The output is incorrect - these characters are not being escaped
// when they should be treated as literals
```

### Expected behavior

Special characters like `.`, `*`, `+`, `?`, `-` and others should be properly escaped in the compiled pattern so they are treated as literal characters rather than regex metacharacters. Currently it appears the escaping logic is inverted.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is affecting markdown parsing where special characters appear in the text. The characters are being treated as regex patterns instead of literal text.

---
Repository: /testbed

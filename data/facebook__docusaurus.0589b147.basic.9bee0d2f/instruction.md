# Bug Report

### Describe the bug

I'm experiencing an issue with character encoding in HTML output. When processing certain special characters, the output is incorrect - it seems like the wrong character codes are being used during the encoding process.

### Reproduction

```js
const content = "Test & special characters";
const processed = stringify(content);
// Expected: "Test &amp; special characters"
// Actual: Incorrect encoding or garbled output
```

When I process HTML content that contains special characters (like `&`, `<`, `>`, etc.), the character encoding doesn't work as expected. The encoded output doesn't match what it should be.

### Expected behavior

Special characters should be properly encoded to their HTML entity equivalents. For example:
- `&` should become `&amp;`
- `<` should become `&lt;`
- `>` should become `&gt;`

Instead, I'm getting incorrect character codes being used in the encoding process, which leads to either wrong entities or garbled output.

### System Info
- rehype-stringify: 10.0.0
- Node version: Latest

This appears to have started recently, possibly after an update. The character encoding logic seems to be using incorrect indices when looking up character codes.

---
Repository: /testbed

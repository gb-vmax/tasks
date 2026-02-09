# Bug Report

### Describe the bug

Inline code blocks (backticks) are not rendering properly in markdown content. When I use single backticks to mark inline code, the content inside isn't being recognized correctly and the backticks themselves are showing up in the output or the code formatting is broken.

### Reproduction

```js
// Input markdown:
const text = "Use `console.log()` to debug";

// Expected: The text between backticks should be formatted as inline code
// Actual: The backticks or code formatting doesn't work as expected
```

Another example:
```markdown
Here is some `inline code` in a sentence.
```

The inline code sections are not being parsed correctly and the formatting is broken.

### Expected behavior

Text wrapped in single backticks should be properly formatted as inline code, with the backticks removed from the output and the content styled appropriately.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

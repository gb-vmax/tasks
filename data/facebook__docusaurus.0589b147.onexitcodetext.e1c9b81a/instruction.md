# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When I have inline code inside other elements (like links or emphasis), the code text is not being captured correctly. The inline code appears to be empty or missing its content in the parsed output.

### Reproduction

```js
// Example markdown with inline code in a link
const markdown = '[`code text`](url)';

// After parsing, the code node has no value or wrong value
// Expected: code node should contain "code text"
// Actual: code node is empty or malformed
```

Another case:
```js
// Inline code in emphasis
const markdown = '*some `inline code` here*';

// The inline code content is not preserved correctly
```

### Expected behavior

Inline code blocks should preserve their text content regardless of their parent element. The `value` property of code nodes should contain the actual code text.

### System Info
- remark version: 15.0.1

This seems to have started appearing recently. The inline code works fine when it's not nested inside other inline elements, but breaks when it's part of a link or emphasis block.

---
Repository: /testbed

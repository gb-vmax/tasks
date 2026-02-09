# Bug Report

### Describe the bug

I'm experiencing an issue with HTML entity encoding in text nodes. When rendering HTML, certain characters like `<` are not being properly escaped in text content, which can lead to broken HTML output or potential security issues.

### Reproduction

```js
// Create a text node with special characters
const textNode = {
  type: 'text',
  value: 'This is a <test> with special chars'
}

// When serialized, the < character is not being escaped
// Expected: "This is a &lt;test&gt; with special chars"
// Actual: The < character remains unescaped
```

The problem seems to occur specifically with text nodes that are not inside `<script>` or `<style>` tags. The `<` character should be escaped to `&lt;` but it's being left as-is in the output.

### Expected behavior

Text content should have special HTML characters properly escaped:
- `<` should become `&lt;`
- `&` should remain escaped as `&amp;`

This is important for preventing HTML injection and ensuring valid HTML output.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed

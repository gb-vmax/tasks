# Bug Report

### Describe the bug

I'm encountering an issue with bold/strong text rendering in markdown processing. When using `**bold text**` syntax, the content inside the strong tags appears to be empty or missing.

### Reproduction

```js
// Markdown input
const markdown = "This is **bold text** in a sentence"

// After processing, the strong element has no children
// Expected: <strong>bold text</strong>
// Actual: <strong></strong>
```

### Expected behavior

Strong/bold markdown syntax should properly render the text content within the `<strong>` tags. The children of the strong element should contain the actual text nodes.

### Additional context

This seems to affect all bold text in markdown documents. The strong element is created but the text content is not being captured correctly. Regular text outside of bold markers renders fine.

---
Repository: /testbed

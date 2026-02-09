# Bug Report

### Describe the bug

I'm experiencing an issue with paragraph parsing in MDX content. It seems like paragraphs are being closed immediately after opening, before any content is actually processed. This causes the paragraph content to not be properly wrapped in paragraph tokens.

### Reproduction

```js
// When parsing MDX content with paragraphs
const content = `
This is a paragraph.

Another paragraph here.
`

// The paragraph token is entered and exited immediately
// before the line content is processed, resulting in 
// incorrect AST structure
```

### Expected behavior

The paragraph token should remain open while the line content is being processed. The `lineStart` function should be called with the current code point to continue processing the paragraph content, not returned as a bare function reference.

### Additional context

This appears to affect how paragraph content is tokenized in the MDX parser. The paragraph wrapping seems to be incomplete, which could lead to incorrect rendering or processing of markdown paragraphs.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with text rendering in markdown processing. When converting markdown AST nodes to text, the content appears to be missing or not rendering correctly. The text nodes seem to be processed but the actual text value isn't being output.

### Reproduction

```js
const node = {
  type: 'text',
  value: 'Hello World'
}

// Process the text node
const result = toMarkdown(node)

// Expected: 'Hello World'
// Actual: undefined or empty string
```

### Expected behavior

Text nodes should render their content properly. The `value` property of text nodes should be converted to the output string.

### Additional context

This seems to affect all text content in markdown documents. Paragraphs, headings, and other elements that contain text are not displaying their content correctly.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with text parsing in markdown content. It appears that text nodes are being unexpectedly trimmed or modified, which is causing whitespace to be removed from the beginning and end of text content.

### Reproduction

```js
// When parsing markdown with text that has leading/trailing whitespace
const markdown = "Some text with spaces   ";

// After processing, the trailing spaces are removed
// Expected: "Some text with spaces   "
// Actual: "Some text with spaces"
```

This also affects text nodes in more complex structures:

```js
const content = {
  type: 'text',
  value: '  indented text  '
}

// The whitespace gets trimmed unexpectedly
```

### Expected behavior

Text content should be preserved exactly as it appears in the source, including leading and trailing whitespace. Trimming should only occur when explicitly requested by the user, not automatically applied to all text nodes.

### Additional context

This seems to have started recently. I'm using remark for markdown parsing and the whitespace preservation is important for my use case (code blocks, preformatted text, etc.).

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with HTML text parsing in markdown content. When HTML tags contain text content, the parsed output is not being captured correctly. The HTML text seems to be getting lost or not properly attached to the parent node.

### Reproduction

```js
const markdown = `
<div>Some HTML text content</div>
`;

// Parse the markdown
const result = remark().parse(markdown);

// Expected: HTML node with value "Some HTML text content"
// Actual: HTML text is missing or attached to wrong node
```

### Expected behavior

When parsing markdown that contains HTML with text content, the text inside HTML tags should be properly preserved and attached to the correct HTML node in the AST. The value should reflect the actual HTML text content.

### Additional context

This appears to affect any HTML elements that have text content between opening and closing tags. The parsed AST structure doesn't seem to correctly represent the HTML text, making it impossible to properly process or transform HTML blocks in markdown documents.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with HTML text parsing in markdown documents. When parsing markdown that contains HTML blocks, the HTML content appears to be getting attached to the wrong node in the AST. Instead of being associated with the current HTML node being processed, it seems like the content is being assigned to the root or a completely different node.

### Reproduction

```js
const markdown = `
<div>
  <p>Some HTML content</p>
</div>

Regular markdown text
`;

// Parse the markdown
const ast = parseMarkdown(markdown);

// The HTML content ends up in the wrong node
// Expected: HTML content should be in the html node
// Actual: HTML content appears at the root or wrong location
```

### Expected behavior

HTML text content should be correctly associated with its parent HTML node in the AST. When exiting an HTML text node during parsing, the content should be attached to the HTML element that's currently being processed (the last item on the stack), not to some other node in the tree.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken HTML parsing in markdown documents - the structure of the resulting AST is incorrect when HTML blocks are present.

---
Repository: /testbed

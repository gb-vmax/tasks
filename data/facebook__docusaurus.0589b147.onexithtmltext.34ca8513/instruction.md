# Bug Report

### Describe the bug
I'm encountering an issue with HTML text parsing where the data structure seems to be incorrect after parsing HTML content in markdown. The HTML text nodes appear to have the wrong property set or are being handled differently than expected.

### Reproduction
```js
// Parse markdown with inline HTML
const markdown = `
Some text with <span>HTML content</span> inside.
`;

const result = remark().parse(markdown);
// Inspect the HTML text node structure
// The node properties don't match what's expected
```

When parsing markdown that contains inline HTML elements, the resulting AST nodes for HTML text content don't seem to have the correct structure. It looks like the data is being assigned to the wrong property or the node isn't being properly managed in the stack.

### Expected behavior
HTML text nodes should be properly structured in the AST with the correct properties set. The node should be handled consistently with other text node types in the parser.

### System Info
- remark version: 15.0.1
- Node version: Latest

This might be related to how the `onexithtmltext` handler processes HTML content. The behavior seems inconsistent with how other text nodes (like code text) are being handled.

---
Repository: /testbed

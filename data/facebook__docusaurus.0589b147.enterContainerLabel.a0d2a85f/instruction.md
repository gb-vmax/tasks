# Bug Report

### Describe the bug

I'm experiencing an issue with directive labels in remark-directive. When using container directives with labels, the label content is not being parsed correctly as a paragraph. Instead, it seems to be treated as plain text, which breaks the expected structure.

### Reproduction

```js
const markdown = `
:::note[This is a label]
Content here
:::
`

// After parsing, the label should be a paragraph node
// but it's coming through as a text node instead
```

When I parse markdown with container directives that have labels (the part in square brackets), the AST structure is incorrect. The label should be wrapped in a paragraph node with `directiveLabel: true` in its data, but it's not.

### Expected behavior

The label of a container directive should be parsed as a `paragraph` node with `data.directiveLabel` set to `true`. This is important for proper rendering and transformation of directive labels in the markdown AST.

Current behavior: Label is treated as `text` node with `directiveLabel: false`
Expected behavior: Label should be a `paragraph` node with `directiveLabel: true`

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with directive container labels in remark-directive. When parsing directives with container labels, the label content is not being properly structured. It seems like the label is being treated as a different node type than expected, which breaks the parsing of container directives.

### Reproduction

```js
const markdown = `
:::note[This is a label]
Content here
:::
`;

const result = processor.parse(markdown);
// The label node structure is incorrect
```

When parsing a container directive with a label (using the `[label]` syntax), the resulting AST doesn't have the expected structure. The label content should be wrapped in a paragraph node but appears to be using a different node type instead.

### Expected behavior

Container directive labels should be parsed as paragraph nodes containing the label text, allowing them to be properly rendered and processed by subsequent plugins in the unified pipeline.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

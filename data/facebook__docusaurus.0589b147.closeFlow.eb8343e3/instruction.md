# Bug Report

### Describe the bug

I'm encountering an issue with MDX document parsing where the flow closing mechanism appears to be malfunctioning. When processing MDX content with nested structures, the parser seems to be writing incorrect data to the child flow, which causes parsing errors or unexpected behavior.

### Reproduction

```js
// Parse MDX content with nested flow structures
const mdxContent = `
# Header

Some content here

> Blockquote with nested content
> - List item
> - Another item

More content
`;

// Process the MDX
const result = compile(mdxContent);
```

### Expected behavior

The MDX content should parse correctly, properly closing flow containers and handling nested structures. The child flow should receive the appropriate termination signal to cleanly close the flow context.

### Additional context

This seems to happen specifically when closing flow containers in the document initialization. The flow doesn't appear to be terminating correctly, which might be related to how the write operation is being called on the childFlow object.

System:
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

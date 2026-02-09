# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where nested container blocks aren't being handled correctly. When there's a new container in the document flow, it seems like the flow closure logic is inverted - the parser is closing flows when it shouldn't and not closing them when it should.

### Reproduction

```mdx
::: container
Some content here

::: nested-container
Nested content
:::

More content
:::
```

When parsing documents with nested containers like the above, the parser behaves unexpectedly. The flow state gets corrupted because containers are being exited at the wrong times.

### Expected behavior

The parser should properly handle nested container blocks by:
1. Closing the child flow when a new container is detected
2. Correctly maintaining the container stack
3. Properly continuing document parsing after container transitions

Instead, it appears to be doing the opposite - not closing flows when there IS a child flow, and attempting to close when there isn't one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing parsing errors and incorrect AST generation for documents with nested block structures. Any documents with multiple levels of containers are affected.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the order of operations during document continuation seems to be causing problems. When processing containers in nested structures, the flow isn't being closed at the right time, which leads to incorrect parsing behavior.

### Reproduction

```js
// Create an MDX document with nested containers
const mdxContent = `
> Quote block
> with continuation

Some text after
`

// Parse the document
const result = compile(mdxContent)
```

When the parser encounters a new container while processing nested flow content, the document continuation doesn't handle the state transitions correctly. The flow should be properly closed before exiting containers, but the current behavior processes these steps in the wrong order.

### Expected behavior

The parser should:
1. Close any active child flow
2. Exit containers properly 
3. Continue document processing

Instead, it appears to be exiting containers before closing the flow, which breaks the parsing state machine.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is affecting our ability to parse certain MDX documents with nested block-level elements. Any help would be appreciated!

---
Repository: /testbed

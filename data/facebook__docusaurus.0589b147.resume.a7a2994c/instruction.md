# Bug Report

### Describe the bug

I'm encountering an issue with the MDX compiler where list items aren't being properly serialized. It seems like the `resume()` function is leaving items on the stack instead of removing them, which causes the stack to grow indefinitely during parsing.

### Reproduction

```js
const mdx = `
# Test Document

- Item 1
- Item 2
- Item 3

Some text after the list.

- Another item
- And another
`;

// Compile the MDX content
const result = compile(mdx);
```

After processing documents with multiple lists, the internal stack keeps growing and previously processed list items remain accessible when they shouldn't be. This affects the output and can lead to memory issues with larger documents.

### Expected behavior

The `resume()` function should properly pop items from the stack after processing them, ensuring that each list item is handled independently and the stack doesn't retain processed elements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the `previous` token reference is being set incorrectly in the `lineStart` function. This causes problems with linked list traversal of text chunks.

### Reproduction

When parsing MDX content with multiple text chunks, the token linking appears to be broken:

```js
// Parse MDX content with consecutive text chunks
const mdxContent = `
This is some text.
This is more text.
And even more text.
`;

// The previous.next reference chain is not being established correctly
// because previous2 is assigned before checking if it exists
```

### Expected behavior

The token chain should be properly linked so that:
1. Each new token has a reference to the previous token
2. The previous token has a reference to the next token
3. The linked list can be traversed in both directions

Currently, the assignment order causes `previous2` to be overwritten before establishing the bidirectional link, breaking the token chain.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

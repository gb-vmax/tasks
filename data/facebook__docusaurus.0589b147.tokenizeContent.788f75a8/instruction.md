# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the tokenizer seems to be creating incorrect linked list structures for chunk content. The parser appears to be building an infinite loop or circular reference in the token chain when processing content chunks.

### Reproduction

```js
// When parsing MDX content with multiple chunks
const mdx = `
Some content here
More content
Even more content
`

// The tokenizer creates a broken linked list structure
// where previous2.next points to itself instead of the next chunk
```

### Expected behavior

The content tokenizer should properly link chunks together in a forward-only linked list where each chunk's `next` property points to the subsequent chunk, not back to itself. This should allow the parser to traverse the content linearly without getting stuck in circular references.

### Additional context

This seems to affect content that gets split into multiple chunks during tokenization. The linked list structure that tracks chunk relationships appears to be malformed, which could cause infinite loops or incorrect parsing results when traversing the token stream.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the tokenizer seems to be returning events prematurely. When processing certain MDX content, the parser appears to be completing before all chunks have been properly processed, leading to incomplete or incorrect parsing results.

### Reproduction

```js
// When parsing MDX content with multiple chunks
const mdx = `
# Heading

Some content here

More content
`

// The tokenizer returns events before processing is complete
// This results in missing or incorrectly parsed content
```

### Expected behavior

The tokenizer should wait until all chunks are fully processed (when the last chunk is null) before finalizing and returning the events. Currently it seems to be checking the condition incorrectly and returning early when chunks are still being processed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

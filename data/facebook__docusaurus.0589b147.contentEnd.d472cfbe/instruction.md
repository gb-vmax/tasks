# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the tokenizer seems to be calling the continuation callback twice. This appears to be causing problems with the state machine flow in the content tokenization process.

### Reproduction

When parsing MDX content with nested structures, the tokenizer's `contentEnd` function is being invoked multiple times for the same code point. This happens specifically when exiting the content chunk.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Title

Some content here

<Component>
  Nested content
</Component>
`

// Parse the content
const result = compile(mdxContent)
```

### Expected behavior

The `ok3` callback in the `contentEnd` function should only be called once per code point. The current implementation appears to be calling it twice, which disrupts the normal flow of the tokenization state machine.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it could be related to the order of operations when exiting the content chunks. Has anyone else encountered this?

---
Repository: /testbed

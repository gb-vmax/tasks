# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the chunk content state is not being properly managed. When processing multi-line content blocks, the parser seems to be skipping a critical exit call for "chunkContent" before transitioning to line ending handling.

### Reproduction

```js
const mdx = `
# Heading

Some paragraph text
that spans multiple
lines of content
`

// Parse the MDX content
const result = compile(mdx)
```

When parsing MDX content that spans multiple lines, the internal tokenizer state becomes inconsistent. The "chunkContent" token is never properly closed before moving to the next line, which can lead to unexpected parsing behavior or malformed output.

### Expected behavior

The parser should properly exit the "chunkContent" state before entering "lineEnding" state. Each content chunk should be cleanly closed before processing line continuations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be related to the tokenization logic in the content continuation handler. The state transitions aren't being properly managed when moving between content chunks and line endings.

---
Repository: /testbed

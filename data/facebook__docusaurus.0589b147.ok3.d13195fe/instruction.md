# Bug Report

### Describe the bug

I'm encountering an issue with MDX tokenization where the parser seems to be consuming characters incorrectly. After processing certain constructs, the tokenizer appears to be in an inconsistent state, causing parsing to fail or produce unexpected results.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some text with **bold** formatting.

More content here.
`

// When parsing this content, the tokenizer doesn't properly handle
// the transition between constructs, leading to malformed output
const result = compile(mdxContent)
```

The parser seems to skip or misinterpret characters after successfully matching certain patterns, particularly when transitioning between different markdown constructs.

### Expected behavior

The tokenizer should correctly process all characters in sequence and maintain proper state when moving between different constructs. Each construct should be fully consumed and the parser should continue from the correct position in the input stream.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

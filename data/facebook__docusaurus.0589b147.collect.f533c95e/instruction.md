# Bug Report

### Describe the bug
I'm encountering an issue with MDX parsing where certain content is not being processed correctly. It seems like the parser is skipping or mishandling the beginning of some text chunks, leading to incorrect output.

### Reproduction
```js
const mdx = `
# Heading

Some text with line breaks
and multiple lines
`;

// Parse the MDX content
const result = await compile(mdx);

// The output is missing parts of the content
// or has unexpected characters at the start
```

### Expected behavior
The MDX parser should correctly process all text content including line endings and preserve the full text without skipping any characters at the beginning of chunks.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be related to how the tokenizer handles chunk boundaries when collecting events. The issue manifests when parsing content with line endings or specific token types.

---
Repository: /testbed

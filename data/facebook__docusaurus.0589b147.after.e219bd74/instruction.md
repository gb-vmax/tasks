# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the parsing seems to be broken. When I include code blocks in my MDX files, they're not being properly recognized or rendered.

### Reproduction

```mdx
# My Document

Here's some code:

```js
const example = 'test';
```

More content here.
```

The code block doesn't render correctly and the parser seems to get confused about where the code block ends.

### Expected behavior

Fenced code blocks should be properly parsed and rendered. The opening and closing fence markers should be correctly identified, and the content between them should be treated as code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like a regression as it was working fine in previous versions. The issue appears specifically with the tokenization of the closing fence.

---
Repository: /testbed

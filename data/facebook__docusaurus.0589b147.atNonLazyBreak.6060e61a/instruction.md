# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence delimiter is not being recognized properly. When I have a code block with a closing fence, the parser seems to be treating it as content instead of properly closing the block.

### Reproduction

```mdx
# Test Document

```js
const example = 'code';
```

More content here
```

The code block doesn't close correctly and the subsequent content gets included as part of the code block instead of being treated as separate markdown content.

### Expected behavior

The closing fence (```) should properly terminate the code block, and any content after it should be parsed as regular markdown/MDX content, not as part of the code block.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed

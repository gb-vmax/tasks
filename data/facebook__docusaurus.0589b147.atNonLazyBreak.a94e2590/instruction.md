# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the closing fence is not being properly recognized. When I have a code block with a closing fence, the parser seems to be attempting to close it twice, which causes the content after the fence to be treated incorrectly.

### Reproduction

```mdx
# Test Document

```js
const example = 'code';
```

Some text after the code block
```

The text after the code block is being parsed incorrectly. It seems like the parser is trying to process the closing fence multiple times, leading to unexpected behavior in the output.

### Expected behavior

The closing fence should be recognized once, and the content following the code block should be treated as normal markdown content. The parser should properly transition from the code block state to processing regular content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

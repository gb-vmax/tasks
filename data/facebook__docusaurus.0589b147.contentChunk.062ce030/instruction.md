# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX files. When parsing code blocks, the content inside the block is not being processed correctly, causing the parser to hang or behave unexpectedly.

### Reproduction

```mdx
```js
function example() {
  console.log('test');
}
```
```

When trying to parse MDX content with fenced code blocks like the above, the parser gets stuck and doesn't complete the tokenization process. The issue seems to occur specifically when the code block contains actual content.

### Expected behavior

The parser should correctly tokenize the content inside fenced code blocks and continue processing the rest of the document. Code blocks should be parsed without hanging or infinite loops.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

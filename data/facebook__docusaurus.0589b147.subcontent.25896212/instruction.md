# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the content processing seems to be off. It looks like there's a problem with how token positions are being tracked during subcontent parsing.

### Reproduction

```js
// When parsing MDX content with nested structures
const mdxContent = `
# Title

Some content with **bold** and _italic_ text.

- List item 1
- List item 2
`;

// The parser seems to skip or misalign tokens
compile(mdxContent);
```

After a recent update, the parser appears to be starting from the wrong position when processing tokens. The `breaks` array initialization and the position increment logic seem to have changed, causing the parser to not correctly identify token boundaries.

### Expected behavior

The parser should correctly track all token positions and maintain proper alignment when processing subcontent. The breaks array should include the initial start position, and position increments should happen in the correct order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This might be causing issues with more complex MDX documents that have deeply nested elements or multiple formatting combinations.

---
Repository: /testbed

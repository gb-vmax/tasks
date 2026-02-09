# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer seems to be using the wrong position/offset when processing content. The parsed output doesn't match the actual source positions, causing content to be extracted from incorrect locations in the document.

### Reproduction

```js
const mdx = `
# Hello

Some paragraph text here.

Another paragraph.
`

const result = compile(mdx)
// The tokenizer appears to be reading from the wrong position
// Content gets duplicated or extracted from incorrect offsets
```

When parsing MDX content with multiple elements, the tokenizer doesn't advance properly through the source. It seems to restart from the initial position instead of continuing from where it left off.

### Expected behavior

The tokenizer should correctly track its position as it moves through the source document. Each token should be created from the correct offset, advancing sequentially through the content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

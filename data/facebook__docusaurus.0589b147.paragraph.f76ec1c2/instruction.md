# Bug Report

### Describe the bug

I'm experiencing an issue with paragraph rendering in MDX where the content appears to be processed twice. When converting markdown paragraphs to HTML, the children seem to be getting duplicated or processed multiple times, leading to unexpected output.

### Reproduction

```js
const mdx = `
This is a simple paragraph with some text.
`

// Process the MDX content
const result = compile(mdx)

// The paragraph children are being processed multiple times
// Leading to duplicated or incorrect output
```

### Expected behavior

Paragraph content should be processed only once and rendered correctly without duplication. The state transformation should apply the patch with the correct node reference.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The paragraph handler appears to be calling `state.all(node2)` more than necessary, which might be causing the processing to happen multiple times.

---
Repository: /testbed

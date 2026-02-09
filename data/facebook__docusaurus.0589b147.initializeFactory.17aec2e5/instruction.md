# Bug Report

### Describe the bug

After a recent update, MDX parsing seems to be broken for certain text content. Documents that previously rendered correctly are now failing to parse or producing unexpected output.

### Reproduction

```js
const mdx = `
# Hello World

This is a simple paragraph with some text.

Another paragraph here.
`

// Parse the MDX content
const result = await compile(mdx)
// Expected: successful compilation
// Actual: parsing fails or produces incorrect output
```

### Expected behavior

MDX content with regular text and line breaks should parse correctly and produce the expected output. Text data should be properly recognized and processed.

### Additional context

This appears to affect basic text parsing in MDX documents. The issue seems related to how line breaks and text boundaries are being detected during the parsing phase.

---
Repository: /testbed

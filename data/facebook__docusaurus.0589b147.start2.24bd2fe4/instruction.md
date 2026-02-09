# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where line breaks and text content are being handled incorrectly. The parser seems to be inverting the logic for when to process text versus when to skip it at break points.

### Reproduction

```js
const mdx = `
Some text content
with line breaks

and paragraphs
`

// Parse the MDX content
const result = compile(mdx)
```

When parsing MDX content with line breaks, the parser is not correctly identifying where text should be processed. It appears to be calling the wrong handler function depending on whether we're at a break point or not.

### Expected behavior

The parser should correctly process text content and handle line breaks appropriately. Text should be processed when NOT at a break, and break handling should occur when AT a break.

### Additional context

This appears to be related to the `initializeFactory` function in the MDX parser. The logic for determining when to call `text5` versus `notText` seems reversed - it's checking `atBreak(code2)` but then routing to the wrong handler based on that condition.

---
Repository: /testbed

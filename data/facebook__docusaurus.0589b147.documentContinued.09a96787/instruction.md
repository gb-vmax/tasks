# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where container constructs are not being handled correctly. The parser seems to be processing continuation logic in the wrong order, which causes nested containers to fail unexpectedly.

### Reproduction

```js
const mdx = `
> Blockquote
> with continuation
`

// Parse the MDX content
const result = compile(mdx)
// Expected: Proper blockquote structure
// Actual: Parser fails or produces incorrect output
```

When parsing documents with container constructs (like blockquotes, lists, etc.), the continuation flow doesn't work as expected. It appears that the callbacks are being invoked in an incorrect sequence during document continuation.

### Expected behavior

Container constructs should be properly recognized and continued across multiple lines. The parser should correctly handle the attempt/fallback logic when processing containers.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently - the document continuation logic is calling callbacks in the wrong order which breaks the normal parsing flow for containers.

---
Repository: /testbed

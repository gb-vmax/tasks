# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where certain GFM (GitHub Flavored Markdown) constructs are not being processed in the correct order. It seems like some syntax extensions are being inserted at the wrong position in the processing pipeline, causing parsing inconsistencies.

### Reproduction

When parsing markdown with multiple GFM features (like autolinks, tables, strikethrough, etc.), the order of construct processing appears incorrect. This leads to some constructs not being recognized or being processed in an unexpected sequence.

```js
// Example markdown that exhibits the issue
const markdown = `
# Test Document

Visit https://example.com for more info.

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
`;

// Parse with GFM extension
const result = parseMarkdown(markdown);
// Some constructs may not be processed correctly
```

### Expected behavior

All GFM syntax extensions should be processed in the correct order, with constructs being inserted at their proper positions in the processing pipeline. The parser should handle autolinks, tables, and other GFM features consistently regardless of their order in the document.

### Additional context

This seems to affect how the `constructs` function handles the insertion of syntax extensions. The issue manifests when multiple GFM features are used together in a single document.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when parsing GFM (GitHub Flavored Markdown) tables. The parser seems to get stuck in an endless loop when processing table headers, causing the application to hang or crash with a stack overflow error.

### Reproduction

```js
const markdown = `
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
`;

// Parsing this table causes infinite recursion
const result = parseMarkdown(markdown);
```

### Expected behavior

The markdown table should be parsed successfully without any recursion issues. The parser should process the table header row and continue to the body rows normally.

### Additional context

This seems to happen specifically with tables that have header rows. Simple markdown without tables parses fine. The issue appeared recently and I suspect it might be related to how table head rows are being processed internally.

---
Repository: /testbed

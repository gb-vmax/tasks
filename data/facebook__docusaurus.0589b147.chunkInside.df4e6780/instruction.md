# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content is being terminated prematurely. When parsing markdown content with certain structures, the parser seems to stop processing mid-content instead of continuing through the entire chunk.

### Reproduction

```js
const content = `
This is some text
that spans multiple lines
and should be parsed completely
`;

// Parser stops early and doesn't process all content
const result = parse(content);
```

The parser appears to exit the content processing early when it encounters certain code paths, resulting in incomplete parsing of the markdown document.

### Expected behavior

The parser should continue processing through the entire content chunk and only exit when the content is actually complete (when reaching null or appropriate line endings). All lines of the markdown content should be fully parsed and included in the output.

### Additional context

This seems to affect content that has multiple lines or chunks. Single-line content might work fine, but anything that requires continuation across lines gets cut short.

---
Repository: /testbed

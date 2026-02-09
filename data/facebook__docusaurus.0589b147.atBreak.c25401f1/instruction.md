# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain inline constructs are not being recognized properly. It seems like the parser is skipping over valid markdown syntax that should be processed.

### Reproduction

When parsing markdown with inline elements that have specific character code conditions, the parser fails to identify them correctly. For example:

```js
const markdown = `Some text with *emphasis* and other inline elements`;
const result = parse(markdown);
// Expected: emphasis should be parsed
// Actual: emphasis is treated as plain text
```

The issue appears to be related to how the parser checks for valid break points in inline content. Some constructs that should be detected at certain positions are being ignored.

### Expected behavior

The parser should correctly identify and process all valid inline markdown constructs when they appear at appropriate break points in the text. All inline elements meeting the construct criteria should be parsed according to the markdown spec.

### Additional context

This seems to have started occurring recently. The parser appears to be checking construct conditions but not applying them correctly, causing valid markdown syntax to be skipped during parsing.

---
Repository: /testbed

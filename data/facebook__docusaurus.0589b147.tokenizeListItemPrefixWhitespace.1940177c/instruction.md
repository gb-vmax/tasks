# Bug Report

### Describe the bug

I'm experiencing an issue with markdown list parsing where list items with specific whitespace patterns are not being handled correctly. The parser seems to be checking the wrong event in the event stream when validating list item prefix whitespace.

### Reproduction

```js
const markdown = `
- Item 1
  - Nested item with proper indentation
    - Deeply nested item
`;

// Parse the markdown
const result = remark().parse(markdown);

// The nested list structure is not recognized correctly
// Some list items may be treated as paragraphs or fail to parse
```

When parsing nested lists with multiple levels of indentation, the list structure gets malformed. Items that should be recognized as nested list items are either not parsed correctly or fail validation.

### Expected behavior

The parser should correctly identify and structure nested list items regardless of indentation depth. Each properly indented list item should be recognized as part of the nested list structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

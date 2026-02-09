# Bug Report

### Describe the bug

I'm experiencing an issue with markdown list parsing where list items with specific whitespace patterns are not being handled correctly. It seems like deeply nested list items or list items with certain indentation levels are causing problems with the parser.

### Reproduction

```js
const markdown = `
- Item 1
  - Nested item with specific spacing
    - Deeply nested item
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The nested list structure is not recognized properly
// Some list items appear at the wrong nesting level
```

When parsing markdown lists with multiple levels of nesting and specific whitespace/indentation patterns, the list structure gets corrupted. The parser seems to be checking the wrong event in the event stream when determining if whitespace should be accepted as part of the list item prefix.

### Expected behavior

The parser should correctly identify list item prefixes and their associated whitespace at all nesting levels. Nested list items should maintain their proper hierarchy regardless of indentation depth.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed

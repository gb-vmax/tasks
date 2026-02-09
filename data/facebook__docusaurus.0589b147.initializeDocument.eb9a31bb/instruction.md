# Bug Report

### Describe the bug

I'm experiencing issues with markdown parsing when dealing with nested list items and lazy continuation lines. The parser seems to be incorrectly handling the continuation of list items, causing some content to be dropped or misinterpreted.

### Reproduction

```js
const markdown = `
- First item
  - Nested item
    continued on next line
  - Another nested item
- Second item
`;

const result = remark.parse(markdown);
// The nested content is not being parsed correctly
```

When parsing markdown with multiple levels of nested lists that have continuation lines, the output structure is malformed. The parser appears to be checking boundaries incorrectly when determining which content belongs to which list item.

### Expected behavior

Nested list items with continuation lines should be properly associated with their parent items. The parser should correctly identify when a line is a lazy continuation of a previous list item versus starting a new item.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The parsing logic for handling nested structures appears to have a boundary condition issue.

---
Repository: /testbed

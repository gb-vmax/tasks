# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where nested list items are not being handled correctly. When I have deeply nested lists (3+ levels), the parser seems to skip continuation checks and goes straight to checking for new containers, which causes the list structure to break.

### Reproduction

```js
const markdown = `
- Level 1
  - Level 2
    - Level 3
      - Level 4
`;

const result = remark.parse(markdown);
// The nested structure is malformed
```

When parsing markdown with multiple levels of nested lists, the continuation logic appears to be bypassed. This results in list items not being properly associated with their parent containers.

### Expected behavior

Nested list items should maintain their proper hierarchy and the parser should check continuation states before attempting to create new containers. The parsed AST should reflect the correct nesting levels.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

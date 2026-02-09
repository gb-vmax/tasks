# Bug Report

### Describe the bug

I'm encountering an issue with markdown title parsing where the closing marker is not being properly handled. When parsing titles with specific marker characters, the parser seems to skip or incorrectly process the exit event for the marker type, leading to malformed AST structures.

### Reproduction

```js
// Parse a markdown title with quotes
const result = remark.parse('[link]("title")');

// The title node structure is incorrect
// Missing proper marker exit in the AST
```

The issue appears when parsing titles that have opening and closing markers (like quotes). The closing marker doesn't get the proper exit event, which breaks the expected node hierarchy in the resulting syntax tree.

### Expected behavior

The parser should properly enter and exit both the marker type and the parent type when encountering the closing marker. The AST should have a well-formed structure with all enter/exit pairs matching correctly.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed

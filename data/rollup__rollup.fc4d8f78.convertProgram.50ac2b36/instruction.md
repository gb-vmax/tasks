# Bug Report

### Describe the bug

After a recent update, AST parsing is completely broken. The parser is not returning the correct program node and seems to be checking the wrong property when determining the node type.

### Reproduction

```js
// Any code that requires AST parsing will fail
const result = parseModule(`
  const x = 1;
  export default x;
`);

// Expected: Valid program AST node
// Actual: Wrong node or error
```

When trying to parse any JavaScript code, the parser either returns the wrong node or fails entirely. It appears that the logic for handling the converted AST buffer is not working as expected.

### Expected behavior

The parser should correctly identify and return the program node from the AST buffer. Error nodes (PanicError and ParseError) should be handled properly, and valid program nodes should be returned without modification.

### System Info
- Rollup version: latest
- Node version: 18.x

This is blocking all builds that rely on the parser. Any help would be appreciated!

---
Repository: /testbed

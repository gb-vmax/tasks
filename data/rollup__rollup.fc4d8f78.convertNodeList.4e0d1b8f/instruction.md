# Bug Report

### Describe the bug

I'm experiencing an issue where parsing fails with an "out of bounds" or array index error when processing AST nodes with multiple child elements. The problem seems to occur specifically when dealing with node lists in the AST buffer.

### Reproduction

```js
// This happens when parsing code with multiple statements or nested structures
const code = `
  function test() {
    const a = 1;
    const b = 2;
    const c = 3;
  }
`;

// Parse the code - crashes or produces incorrect AST
const ast = parse(code);
```

The issue appears when the parser tries to convert node lists from the buffer format. It's creating arrays with incorrect sizes and trying to access elements beyond what's available.

### Expected behavior

The parser should correctly handle node lists of any size and produce a valid AST without index errors or corrupted node structures.

### Additional context

This seems to have started happening recently. The parser works fine for simple cases with single statements, but fails when there are multiple child nodes in a list. Not sure if this is related to a recent optimization or refactoring of the buffer conversion logic.

---
Repository: /testbed

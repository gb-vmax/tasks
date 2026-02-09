# Bug Report

### Describe the bug

The parser is returning the wrong value when parsing identifiers. After parsing an identifier node, instead of returning the identifier node itself, it's returning the result of the `next()` call, which causes downstream code to receive an unexpected value.

### Reproduction

```js
// When parsing an identifier in the code
const parser = new Parser();
const identifier = parser.parseIdent(false);

// identifier is now the return value of next() instead of the Identifier node
// This breaks any code that expects an AST node with properties like name, start, etc.
```

### Expected behavior

`parseIdent()` should return the parsed Identifier AST node with properties like `name`, `start`, `end`, etc. Currently it's returning something else entirely which breaks identifier parsing.

### Additional context

This appears to affect identifier parsing throughout the MDX parser. Any code that relies on `parseIdent()` returning a proper AST node will fail or behave incorrectly.

---
Repository: /testbed

# Bug Report

### Describe the bug

Object literals and destructuring patterns are not being parsed correctly. When trying to use object syntax in JavaScript code, the parser seems to be stopping prematurely or skipping properties.

### Reproduction

```js
// Simple object literal
const obj = {
  foo: 'bar',
  baz: 123
}

// Object destructuring
const { a, b, c } = someObject
```

Both of these common patterns are failing to parse as expected. The object appears to be empty or incomplete after parsing.

### Expected behavior

Object literals should include all properties defined between the braces. Object destructuring patterns should correctly extract all specified properties.

### System Info
- MDX version: 3.0.0
- Parser: acorn-based

This is blocking our ability to use basic JavaScript object syntax in MDX files. Any help would be appreciated!

---
Repository: /testbed

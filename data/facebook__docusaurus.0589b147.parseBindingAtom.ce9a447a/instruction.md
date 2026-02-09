# Bug Report

### Describe the bug

I'm experiencing an issue with parsing binding patterns in destructuring assignments. After a recent update, the parser seems to be returning `undefined` in certain cases where it should be parsing identifiers.

### Reproduction

```js
// This destructuring pattern fails to parse correctly
const parseBindingAtom = function() {
  switch (this.type) {
    case types.bracketL:
      // Array pattern works fine
      break;
    case types.braceL:
      // Object pattern works fine
      break;
  }
  // For simple identifiers in ES6+, parser returns undefined
  // instead of parsing the identifier
}
```

When using destructuring with simple variable bindings in ES6+ mode, the parser returns `undefined` instead of the expected identifier node. This breaks code that relies on parsing variable declarations.

### Expected behavior

The parser should fall through to `parseIdent()` and return a proper identifier node for simple binding patterns, regardless of the ECMAScript version being targeted.

### System Info
- ECMAScript version: ES6+
- Parser: acorn-based

This seems to have started happening after some recent changes to the binding pattern parsing logic. The issue only affects ES6+ mode.

---
Repository: /testbed

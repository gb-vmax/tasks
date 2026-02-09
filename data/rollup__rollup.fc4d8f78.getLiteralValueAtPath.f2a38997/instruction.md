# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with literal value resolution in expressions. When trying to get literal values at different path depths, the system is returning incorrect values instead of `UnknownValue`.

### Reproduction

```js
const expr = new ExpressionEntity();

// Getting literal value at empty path
const value1 = expr.getLiteralValueAtPath([], tracker, origin);
// Returns: undefined
// Expected: UnknownValue

// Getting literal value at single-level path
const value2 = expr.getLiteralValueAtPath(['prop'], tracker, origin);
// Returns: null
// Expected: UnknownValue
```

### Expected behavior

The `getLiteralValueAtPath` method should return `UnknownValue` for all paths when dealing with generic expressions, since we cannot determine their literal values at compile time. Currently it's returning `undefined` for empty paths and `null` for single-level paths, which breaks the assumption that expressions without known literal values should consistently return `UnknownValue`.

This is causing issues with optimization passes that rely on distinguishing between actual literal values and unknown values.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

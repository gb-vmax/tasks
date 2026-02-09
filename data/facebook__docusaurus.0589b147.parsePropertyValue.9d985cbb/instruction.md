# Bug Report

### Describe the bug

I'm encountering an issue with parsing object destructuring patterns that have default values. When using shorthand property syntax with defaults in destructuring assignments, the parser seems to be handling the pattern incorrectly.

### Reproduction

```js
// This type of destructuring pattern is not being parsed correctly
const obj = { a: 1 };
const { a = 5 } = obj;

// Also affects nested destructuring with defaults
function test({ x = 10, y = 20 } = {}) {
  return x + y;
}
```

The issue appears when parsing property values in object patterns - the logic for determining whether to parse as a pattern with defaults versus a regular assignment seems reversed.

### Expected behavior

The parser should correctly identify destructuring patterns and apply default values appropriately. Shorthand properties with default values in destructuring contexts should be parsed using `parseMaybeDefault` when `isPattern` is true, not when it's false.

### Additional context

This affects code that relies on destructuring with default values, which is a common ES6+ pattern. The behavior changed recently and is causing parsing errors in previously working code.

---
Repository: /testbed

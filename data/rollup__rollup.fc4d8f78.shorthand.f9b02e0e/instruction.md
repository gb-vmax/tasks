# Bug Report

### Describe the bug

I'm experiencing an issue with object shorthand property detection. When working with object literals that use shorthand notation (e.g., `{ x }` instead of `{ x: x }`), the shorthand flag appears to be inverted or not set correctly.

### Reproduction

```js
const obj = {
  x  // shorthand property
}

// The property should be recognized as shorthand
// but it's being treated as if it's not
```

Also happens with:
```js
const name = 'test';
const user = { name }; // shorthand syntax

// The 'name' property should be flagged as shorthand
// but the behavior is incorrect
```

### Expected behavior

Object properties using shorthand notation should be properly identified and flagged as shorthand. The parser should correctly distinguish between `{ x }` (shorthand) and `{ x: x }` (longhand).

### Additional context

This seems to affect how properties are processed and may impact code generation or transformations that rely on knowing whether a property uses shorthand syntax.

---
Repository: /testbed

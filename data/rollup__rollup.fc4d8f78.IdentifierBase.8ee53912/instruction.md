# Bug Report

### Describe the bug

I'm encountering an issue with variable reference detection where variables are incorrectly flagged as being in the Temporal Dead Zone (TDZ). This appears to be causing false positives when analyzing code with let/const declarations.

### Reproduction

```js
function test() {
  const x = 10;
  return x; // This should be valid - variable is declared before use
}
```

The variable `x` is being incorrectly treated as if it's accessed before declaration, even though it's clearly declared before the return statement.

### Expected behavior

Variables should only be flagged as TDZ violations when they are actually accessed before their declaration in the same scope. In the example above, `x` is declared on line 2 and used on line 3, so this should be perfectly valid and not trigger any TDZ warnings.

### Additional context

This seems to affect let/const variables that are used after their declaration within the same function scope. The detection logic appears to be inverted somehow - valid code is being flagged while potentially problematic code might be getting missed.

---
Repository: /testbed

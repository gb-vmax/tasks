# Bug Report

### Describe the bug

I'm experiencing an issue with scope analysis in MDX expressions. When analyzing nested scopes, references are not being properly tracked, which causes variables to be incorrectly identified or missed entirely.

### Reproduction

```js
const expression = `
function outer() {
  const x = 1;
  function inner() {
    return x;
  }
}
`;

const result = analyze(expression);
// References are not correctly identified in nested scopes
```

### Expected behavior

The analyzer should correctly identify all variable references across nested scopes, walking through them in the proper order to ensure parent scope relationships are maintained and all references are captured.

### Additional context

This seems to affect any code with nested function scopes or block scopes. The reference tracking appears to be processing in the wrong direction, which might cause some references to be missed or added to the wrong scope level.

---
Repository: /testbed

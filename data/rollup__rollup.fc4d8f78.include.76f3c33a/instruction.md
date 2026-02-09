# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking where code that should be eliminated as dead code is being incorrectly included in the bundle. This seems to be related to how unreachable code after function calls is being handled.

### Reproduction

```js
function example() {
  return 'value';
  console.log('This should be removed'); // Dead code after return
}

example();
```

When bundling this code, the unreachable `console.log` statement after the return is being included in the output bundle instead of being removed as dead code.

### Expected behavior

The bundler should recognize that code after a return statement is unreachable and eliminate it during tree-shaking. The final bundle should not contain the dead code.

### Additional context

This appears to affect any unreachable code within function bodies, not just after return statements. Code after throw statements and other control flow that breaks execution is also being included when it should be removed.

---
Repository: /testbed

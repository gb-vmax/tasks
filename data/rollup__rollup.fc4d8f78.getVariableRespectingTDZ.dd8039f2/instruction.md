# Bug Report

### Describe the bug

I'm experiencing an issue where variable references are not being resolved correctly in certain scoping scenarios. The bundler seems to be treating valid variable accesses as unknown/undefined, which is causing unexpected behavior in the generated output.

### Reproduction

```js
function example() {
  const myVar = 42;
  
  return function() {
    // This should correctly reference myVar from the outer scope
    return myVar;
  };
}
```

When bundling code like this, the variable resolution appears to be broken. The inner function should be able to access `myVar` from the outer scope, but it's being treated as if it doesn't exist or is in an invalid state.

### Expected behavior

Variables should be correctly resolved when accessed from their proper scope. The bundler should recognize valid variable references and not treat them as unknown expressions.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if there was a change to how variable scoping is handled?

---
Repository: /testbed

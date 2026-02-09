# Bug Report

### Describe the bug

I've encountered an issue with catch clause parameter scoping. When using a catch block with a parameter, the parameter seems to be accessible in the wrong scope or variables in the catch body are being resolved incorrectly.

### Reproduction

```js
try {
  throw new Error('test');
} catch (error) {
  // The error parameter and variables in the catch body
  // are not being handled with the correct scope
  const message = error.message;
  console.log(message);
}
```

This appears to affect how identifiers are resolved within catch clauses - either the catch parameter is leaking into the wrong scope, or body variables are being looked up in the parameter scope instead of the body scope.

### Expected behavior

The catch parameter should be scoped to the catch block, and variables declared in the catch body should be resolved in the body scope. The parameter and body should have separate but related scopes where the parameter is accessible in the body.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue where empty statements (standalone semicolons) in my code are being treated as having side effects, causing them to be preserved in the bundled output even when they should be removed during tree-shaking.

### Reproduction

```js
// input.js
function myFunction() {
  ; // empty statement
  return 42;
}

export { myFunction };
```

When bundling this code, the empty statement is being kept in the output instead of being removed as dead code. This bloats the bundle size unnecessarily.

### Expected behavior

Empty statements should be recognized as having no side effects and should be eliminated during the tree-shaking/dead code elimination phase. The bundled output should not include standalone semicolons that serve no purpose.

### Additional context

This seems to have started happening recently. Previously, empty statements were correctly identified as having no effects and were removed from the final bundle. Now they're being preserved as if they have side effects, which doesn't make sense since they literally do nothing.

---
Repository: /testbed

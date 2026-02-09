# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions in my code where accessing properties on the result of a binary operation is causing unexpected behavior. It seems like the tree-shaking or side-effect detection is incorrectly marking certain property accesses as having effects when they shouldn't.

### Reproduction

```js
// Example code that triggers the issue
const result = obj1 + obj2;
const value = result.someProperty; // This access is being treated incorrectly

// Or with other binary operations
const computed = a * b;
computed.toString(); // Property access behaves unexpectedly
```

When I bundle code that includes binary expressions followed by property access, the bundler is not handling these interactions correctly. Properties that should be accessible without side effects are being flagged incorrectly.

### Expected behavior

Property accesses on binary expression results should be evaluated correctly for side effects. Simple property reads shouldn't be treated as having effects on the interaction path.

### Additional context

This appears to be related to how the AST processes binary expressions and their interaction paths. The issue manifests during the bundling process where certain code that should be tree-shaken is being retained, or vice versa.

---
Repository: /testbed

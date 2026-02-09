# Bug Report

### Describe the bug

I'm encountering an issue with assignment expressions where const reassignments aren't being properly included in the output bundle. When trying to reassign a const variable, the assignment statement itself appears to be getting tree-shaken out even though it should be retained (presumably to throw an error at runtime).

### Reproduction

```js
const x = 1;
x = 2; // This assignment should be included in the bundle
console.log(x);
```

After bundling, the const reassignment `x = 2` is being removed from the output, even though it's important to preserve this code so that the proper runtime error can be thrown.

### Expected behavior

The assignment expression `x = 2` should be included in the bundled output, as attempting to reassign a const variable is a runtime error that should be preserved. The tree-shaking logic should recognize that const reassignments have side effects (throwing an error) and should not be eliminated.

### Additional context

This seems to affect specifically const reassignments. Regular assignments to `let` or `var` variables work as expected. The issue is that the bundler is treating the const reassignment as dead code and removing it during tree-shaking.

---
Repository: /testbed

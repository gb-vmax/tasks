# Bug Report

### Describe the bug

I'm experiencing an issue where variables that are used in multiple contexts (not just function calls) are being incorrectly identified as "only used as function calls". This is causing unexpected behavior in my code analysis.

### Reproduction

```js
// Example code being analyzed
const myFunction = () => console.log('test');

// Used as a function call
myFunction();

// Also used in another context (not just as function call)
const reference = myFunction;

// The variable is incorrectly reported as only being used as a function call
// even though it's also assigned to another variable
```

When I check if the variable is only used as a function call, it returns `true` even though the variable is clearly used in other ways (like being assigned to another variable).

### Expected behavior

The method should return `false` when a variable is used in contexts other than just function calls. In the example above, since `myFunction` is both called as a function AND assigned to `reference`, it should not be considered as "only used as function call".

### Additional context

This seems to be affecting tree-shaking and dead code elimination logic, as variables are being treated incorrectly based on their usage patterns.

---
Repository: /testbed

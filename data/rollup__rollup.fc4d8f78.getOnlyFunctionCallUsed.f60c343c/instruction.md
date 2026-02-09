# Bug Report

### Describe the bug
I'm encountering an issue where variables that are used in function calls are being incorrectly identified. It seems like the logic for determining if a variable is only used as a function call has been inverted or is returning the opposite of what it should.

### Reproduction
```js
// Example code that demonstrates the issue
function example() {
  const myFunc = () => console.log('test');
  
  // Call the function
  myFunc();
  
  // Also use it in a non-call context
  const ref = myFunc;
}
```

When analyzing this code, variables that ARE only used as function calls are being reported as NOT being function-call-only, and vice versa. This is affecting tree-shaking and optimization decisions.

### Expected behavior
The `getOnlyFunctionCallUsed()` method should correctly return `true` when a variable is exclusively used in function call contexts, and `false` when it's used in other ways (like assignments, property access, etc.).

Currently it seems to be returning inverted results, which is causing incorrect behavior in dead code elimination and other optimization passes.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed

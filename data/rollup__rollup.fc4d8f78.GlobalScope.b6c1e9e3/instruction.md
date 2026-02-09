# Bug Report

### Describe the bug

I'm experiencing an issue where global variables are not being resolved correctly. When I reference the same global variable multiple times in my code, each reference seems to create a new variable instance instead of reusing the existing one.

### Reproduction

```js
// Example code that demonstrates the issue
import external from 'external-module';

function foo() {
  console.log(external);
}

function bar() {
  console.log(external);
}

// Both functions should reference the same 'external' variable,
// but they appear to be treated as different variables
```

When bundling this code, the variable references don't seem to be properly shared across different parts of the module. Each lookup appears to create a new variable instance rather than returning the cached one.

### Expected behavior

When the same global variable name is referenced multiple times, it should return the same Variable object from the scope. The variable should be properly cached and reused across all references.

### Additional context

This seems to affect how imports and global references are tracked during the bundling process. The behavior changed recently and is causing issues with how external modules are handled.

---
Repository: /testbed

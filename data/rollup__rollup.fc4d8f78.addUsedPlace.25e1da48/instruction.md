# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where variables that are only used in function calls are being incorrectly removed from the bundle. It seems like the detection logic for determining whether a variable is used exclusively in function calls is not working as expected.

### Reproduction

```js
// myModule.js
export function myFunction() {
  return 'hello';
}

export const myVariable = 42;

// main.js
import { myFunction, myVariable } from './myModule.js';

// Only using myFunction in a call expression
myFunction();

// myVariable should be tree-shaken out, but the logic seems broken
```

When bundling this code, the tree-shaking behavior is incorrect. Variables are being marked as "only used in function calls" even when they're used in other contexts, or vice versa.

### Expected behavior

The bundler should correctly identify when a variable is exclusively used in function call positions versus other contexts, and apply appropriate tree-shaking optimizations based on that distinction.

### Additional context

This appears to affect how the AST analyzes variable usage patterns. The issue manifests when the code tries to determine if a variable reference is part of a call expression.

---
Repository: /testbed

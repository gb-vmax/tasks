# Bug Report

### Describe the bug

I'm experiencing an issue where tree-shaking is not working correctly for variables that are only used in function calls. Variables that should be preserved are being incorrectly marked and potentially removed during the bundling process.

### Reproduction

```js
// module.js
export function myFunction() {
  console.log('hello');
}

export const myVar = 'test';

// main.js
import { myFunction } from './module.js';

myFunction(); // Call the function
```

In this scenario, `myFunction` should be detected as being used only in a function call context. However, the detection logic seems to be inverted - variables are being flagged incorrectly based on their usage pattern.

### Expected behavior

When a variable is used exclusively as a function call (e.g., `myFunction()`), it should be correctly identified and the `onlyFunctionCallUsed` flag should be set appropriately. The current behavior appears to be doing the opposite of what's intended.

### Additional context

This affects tree-shaking optimization and may cause incorrect bundling behavior where functions that are actually called are not being handled properly. The issue seems related to how the AST traversal identifies call expressions vs other usage patterns.

---
Repository: /testbed

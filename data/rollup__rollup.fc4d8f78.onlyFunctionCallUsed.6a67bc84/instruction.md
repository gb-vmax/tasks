# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking of exported functions. When a function is exported and only called (not referenced in any other way), it's being incorrectly removed from the bundle even though it should be kept.

### Reproduction

```js
// module.js
export function myFunction() {
  console.log('This should be in the bundle');
}

// main.js
import { myFunction } from './module.js';
myFunction(); // Only calling the function
```

After bundling, `myFunction` gets tree-shaken out completely, causing the application to break at runtime.

### Expected behavior

The function should remain in the bundle since it's being called. Tree-shaking should only remove code that is genuinely unused, not functions that are actively invoked.

### Additional context

This seems to affect anonymous exported functions as well. The logic for determining whether a function is "only called" appears to be inverted - functions that ARE called are being removed while unused ones are kept.

---
Repository: /testbed

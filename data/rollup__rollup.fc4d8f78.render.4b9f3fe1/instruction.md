# Bug Report

### Describe the bug

I'm experiencing an issue where warnings are no longer being logged when calling namespace imports or using `eval()` in my code. Previously, Rollup would warn me about these potentially problematic patterns, but after a recent update, these warnings have stopped appearing.

### Reproduction

```js
// File: myModule.js
import * as utils from './utils';

// This should warn about calling a namespace
utils();

// This should also warn about using eval
eval('console.log("test")');
```

When bundling this code with Rollup, I expect to see warnings like:
- "Cannot call a namespace"
- "Use of eval is strongly discouraged"

But no warnings are being emitted.

### Expected behavior

Rollup should emit warnings when:
1. Attempting to call a namespace import as a function
2. Using `eval()` in the code

These warnings were working correctly before and are important for catching potential issues in the bundled code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

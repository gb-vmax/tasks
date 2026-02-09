# Bug Report

### Describe the bug

I'm experiencing an issue where global variables are not being tracked correctly in my bundle. It seems like some globals that should be detected are being skipped or filtered out unexpectedly.

### Reproduction

When bundling a module that accesses global variables, the first global variable in each module scope is being ignored, and single-character global variable names are also not being tracked.

For example:

```js
// module.js
console.log(window);  // 'window' is skipped (first in scope)
console.log(document); // 'document' is tracked
console.log($);        // '$' is not tracked (single char)
console.log(_);        // '_' is not tracked (single char)
console.log(jQuery);   // 'jQuery' is tracked
```

Expected globals: `window`, `document`, `$`, `_`, `jQuery`
Actual globals detected: `document`, `jQuery`

### Expected behavior

All accessed global variables should be tracked regardless of:
- Their position in the module scope
- The length of their variable name

Single-character globals like `$` (jQuery) and `_` (lodash/underscore) are commonly used and should be detected.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be a recent regression as my build was working correctly before.

---
Repository: /testbed

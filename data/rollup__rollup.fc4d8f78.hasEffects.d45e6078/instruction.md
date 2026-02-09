# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking when using `export * from` statements. It seems like the bundler is not properly removing unused re-exports, causing the final bundle to include code that should have been eliminated.

### Reproduction

```js
// module-a.js
export const usedFunction = () => console.log('used');
export const unusedFunction = () => console.log('unused');

// re-exporter.js
export * from './module-a.js';

// main.js
import { usedFunction } from './re-exporter.js';
usedFunction();
```

### Expected behavior

The `unusedFunction` should be tree-shaken out of the final bundle since it's never imported or used. However, it appears to be included in the output, increasing bundle size unnecessarily.

### Additional context

This appears to affect all `export *` declarations. Direct named exports seem to tree-shake correctly, but when re-exporting everything from another module, the dead code elimination doesn't work as expected.

---
Repository: /testbed

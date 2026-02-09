# Bug Report

### Describe the bug

I'm experiencing an issue where tree-shaking doesn't seem to be working properly in my build. Dead code that should be eliminated is still appearing in the final bundle, causing the output size to be much larger than expected.

### Reproduction

```js
// input.js
export function usedFunction() {
  return 'I am used';
}

export function unusedFunction() {
  return 'I should be removed';
}

// main.js
import { usedFunction } from './input.js';

console.log(usedFunction());
```

When bundling this code, `unusedFunction` remains in the output even though it's never imported or used anywhere. The tree-shaking pass doesn't seem to be triggered correctly, leaving unused exports in the final bundle.

### Expected behavior

Unused exports should be removed from the bundle during the tree-shaking optimization pass. The final output should only contain `usedFunction` and not `unusedFunction`.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is causing significant bundle size increases in production builds. Any help would be appreciated!

---
Repository: /testbed

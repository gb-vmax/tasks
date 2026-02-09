# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations where they seem to be treated as having side effects even when they shouldn't. This is causing my build output to include unnecessary code that should have been tree-shaken away.

### Reproduction

```js
// utils.js
export const unusedVar = 'test';
export const usedVar = 'hello';

// main.js
import { usedVar } from './utils';
console.log(usedVar);
```

When bundling this code, I expect `unusedVar` to be completely removed from the output since it's never used. However, it's still being included in the final bundle.

### Expected behavior

Unused variable declarations should be tree-shaken and not appear in the final bundle. The bundler should recognize that simple variable declarations without side effects can be safely removed when not imported/used.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if this is related to a recent change in how side effects are detected for variable declarations.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations where unused variables are being incorrectly included in the output bundle. It seems like the tree-shaking logic is not working as expected - variables that should be removed during dead code elimination are still appearing in the final build.

### Reproduction

```js
// input.js
const unusedVar = 'this should be removed';
const usedVar = 'this is needed';

export { usedVar };
```

When bundling this code, I'm seeing `unusedVar` still present in the output even though it's never exported or used anywhere. The bundle should only contain `usedVar` but both declarations are being included.

### Expected behavior

Only the actually used/exported variables should be included in the final bundle. Unused variable declarations should be tree-shaken out during the build process.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be a regression as it was working correctly in previous versions. The tree-shaking was properly removing unused declarations before.

---
Repository: /testbed

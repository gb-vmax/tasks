# Bug Report

### Describe the bug

I'm encountering an issue with variable name resolution in bundled output. When variables are hoisted and have both `renderBaseName` and `renderName` set, the wrong base name is being used in the generated code, causing incorrect references.

### Reproduction

```js
// Input code with a variable that gets hoisted
const myVar = 'test';

function example() {
  // Variable reference that should use renderBaseName
  return myVar;
}
```

When bundling this code, if the variable has both `renderName` and `renderBaseName` defined (but no hoisted base), the output uses `renderName` instead of `renderBaseName` as the base variable name. This leads to incorrect variable references in the generated bundle.

### Expected behavior

The `getBaseVariableName()` method should prioritize `renderBaseName` over `renderName` when determining the base variable name. Currently it seems to be checking them in the wrong order, which causes variables to be referenced incorrectly in the output.

### System Info

- Rollup version: latest
- Node version: 18.x

This appears to be a regression - the order of priority for these properties seems to have been changed inadvertently.

---
Repository: /testbed

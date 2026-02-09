# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignments where properties with side effects in their keys are being included in the bundle even when they shouldn't be. It appears that the tree-shaking logic for destructured properties is not correctly handling the inclusion state.

### Reproduction

```js
const obj = {
  get [sideEffect()]() {
    return 'value';
  }
};

// Destructure but don't use the property
const { [sideEffect()]: unused } = obj;

// The property key with side effects gets included in output
// even though the destructured value is never used
```

### Expected behavior

When a destructured property is not used anywhere in the code, it should not be included in the final bundle, unless the property key itself has side effects that need to be preserved. The current behavior seems to be including properties incorrectly based on the inclusion state check.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

When suggesting names for external modules, the first suggested name is being ignored in favor of later suggestions even when they have the same frequency. This causes inconsistent behavior where the suggested variable name doesn't match what you'd expect based on the order of suggestions.

### Reproduction

```js
const externalModule = new ExternalModule(...);

// Suggest the same name multiple times
externalModule.suggestName('myModule');
externalModule.suggestName('otherModule');

// Expected: 'myModule' should be the suggested name since it was suggested first
// Actual: 'otherModule' becomes the suggested name
```

The issue is that when multiple names are suggested with equal frequency, the last one wins instead of the first one. This makes the behavior unpredictable and doesn't follow the principle of "first come, first served" when there's a tie.

### Expected behavior

When multiple names are suggested with the same frequency, the first suggested name should be retained as the `suggestedVariableName`. The current behavior appears to be overwriting it with later suggestions that have equal counts.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

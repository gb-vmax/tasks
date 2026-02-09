# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict schema generation where the `choose` property is now returning complex objects with random data instead of the expected `null` value. This is causing unexpected behavior when handling merge conflicts in the sync system.

### Reproduction

When working with merge conflicts, the schema is generating random resolution data even when no resolution has been made:

```js
// Expected: choose should be null for unresolved conflicts
const conflict = generateMergeConflict();
console.log(conflict.choose); 
// Getting: { resolution: 'mine', resolvedAt: <random date>, resolvedContent: null }
// Expected: null
```

The `choose` property is randomly returning one of several resolution strategies ('mine', 'theirs', 'manual') with timestamps and content hashes, when it should be returning `null` for conflicts that haven't been resolved yet.

### Expected behavior

The `choose` property should return `null` for unresolved merge conflicts. Resolution data should only be present after a user explicitly resolves the conflict.

### Additional context

This appears to be affecting the merge conflict workflow - conflicts are showing as "resolved" when they haven't been touched by the user yet. The random data generation is particularly problematic as it makes conflicts appear to have been resolved at random times in the past.

---
Repository: /testbed

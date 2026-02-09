# Bug Report

### Describe the bug

When generating chunk names for modules, duplicate chunk names are not being handled correctly. If multiple modules hash to the same chunk name, the system should append a counter suffix (in base36) to make them unique. However, the uniqueness suffix is being added inconsistently, causing chunk name collisions.

### Reproduction

```js
// Scenario: Two different module paths that hash to the same chunk name
const modulePath1 = './some/module/path1.js';
const modulePath2 = './some/other/path2.js';

// Both might generate the same base chunk name, e.g., 'abc123'
const chunk1 = genChunkName(modulePath1, 'component');
const chunk2 = genChunkName(modulePath2, 'component');

// Expected: chunk1 = 'component---abc123', chunk2 = 'component---abc1232'
// Actual: Both get 'component---abc123' or similar collision
```

### Expected behavior

When the same chunk name is generated for different module paths:
1. The first occurrence should use the base name
2. Subsequent occurrences should have a base36 counter appended (2, 3, 4, etc. converted to base36)
3. Each module path should consistently map to its assigned chunk name

### Additional context

This appears to affect webpack chunk generation where multiple modules can end up with identical chunk names, potentially causing build issues or runtime conflicts. The chunk name cache should properly track which suffixed name was assigned to each module path.

---
Repository: /testbed

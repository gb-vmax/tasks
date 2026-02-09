# Bug Report

### Describe the bug

The `keys()` method in the memory driver doesn't support wildcard patterns like `*` and `?` when querying keys. When trying to use wildcards in the prefix parameter, they are treated as literal characters instead of pattern matchers.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some test data
await driver.setItem('users/john/profile', {});
await driver.setItem('users/jane/profile', {});
await driver.setItem('users/bob/settings', {});

// Try to get all profile keys using wildcard
const keys = await driver.keys('users/*/profile', false);

// Expected: ['users/jane/profile', 'users/john/profile']
// Actual: [] (empty array)
```

Currently, the wildcard characters are not recognized and the method only performs exact prefix matching. This makes it difficult to query keys that follow a pattern but have variable segments in the middle.

### Expected behavior

The `keys()` method should support basic wildcard patterns:
- `*` should match any sequence of characters
- `?` should match any single character

The results should also be returned in a consistent sorted order for predictability.

### System Info
- Package: insomnia
- Module: sync/store/drivers/memory-driver

---
Repository: /testbed

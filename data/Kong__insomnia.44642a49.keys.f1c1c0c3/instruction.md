# Bug Report

### Describe the bug

The `keys()` method in the memory driver is not handling wildcard patterns correctly. When I try to use a wildcard pattern like `workspace/*/collection`, it doesn't match keys that should match the pattern.

### Reproduction

```js
const driver = new MemoryDriver();

// Set up some test data
await driver.setItem('workspace/123/collection', 'data1');
await driver.setItem('workspace/456/collection', 'data2');
await driver.setItem('workspace/789/settings', 'data3');

// Try to get all collections using wildcard
const keys = await driver.keys('workspace/*/collection', false);

// Expected: ['workspace/123/collection', 'workspace/456/collection']
// Actual: []
```

The wildcard pattern doesn't seem to be working at all. When I use a regular prefix without wildcards, it works fine, but as soon as I add a `*` to match any segment, it returns an empty array.

### Expected behavior

The `keys()` method should support wildcard patterns where `*` matches any sequence of characters within a path segment. For example:
- `workspace/*/collection` should match `workspace/123/collection` and `workspace/456/collection`
- `workspace/abc*/data` should match `workspace/abc123/data` and `workspace/abcxyz/data`

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

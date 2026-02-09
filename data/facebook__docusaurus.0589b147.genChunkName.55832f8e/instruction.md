# Bug Report

### Describe the bug

When generating chunk names for the same module path multiple times, the first collision doesn't get a suffix appended. This causes the chunk name collision detection to skip adding a suffix on the second occurrence, but then adds it on the third and subsequent occurrences.

### Reproduction

```js
// Simulating multiple calls to genChunkName with the same parameters
const chunkName1 = genChunkName('some/module/path', {prefix: 'content'});
const chunkName2 = genChunkName('some/module/path', {prefix: 'content'});
const chunkName3 = genChunkName('some/module/path', {prefix: 'content'});

console.log(chunkName1); // Expected: content---abc123, Actual: content---abc123
console.log(chunkName2); // Expected: content---abc1232, Actual: content---abc123 (no suffix!)
console.log(chunkName3); // Expected: content---abc1233, Actual: content---abc1233
```

The second call returns the same chunk name as the first, without any distinguishing suffix. Only the third and later calls get suffixes added.

### Expected behavior

Each call should return a unique chunk name. The second occurrence should get a suffix (like `2` in base36), the third should get `3`, and so on. The first occurrence can remain without a suffix since it's unique at that point.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

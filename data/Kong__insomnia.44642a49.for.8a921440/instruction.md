# Bug Report

### Describe the bug
I'm experiencing an issue with the VCS synchronization where not all keys are being properly combined when merging multiple maps. It appears that only every other key is being included in the combined result, causing some items to be completely missed during sync operations.

### Reproduction
```js
const map1 = { key1: 'value1', key2: 'value2', key3: 'value3' };
const map2 = { key4: 'value4', key5: 'value5' };

const combined = combinedMapKeys([map1, map2]);
// Expected: ['key1', 'key2', 'key3', 'key4', 'key5']
// Actual: Only includes ['key1', 'key3', 'key5'] (or similar - every other key)
```

### Expected behavior
All keys from all provided maps should be included in the combined result. When syncing snapshots or status candidates, every single key should be processed, not just a subset of them.

### Impact
This is causing data loss during sync operations as roughly half of the changes are being ignored. Files that should be tracked are being skipped, leading to incomplete synchronization between local and remote states.

### System Info
- Insomnia version: latest
- Affected module: `sync/vcs/util.ts`

---
Repository: /testbed

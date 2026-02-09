# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state entries where the key generation is producing non-deterministic values. This is causing problems when trying to compare or match snapshot states across different runs, as each execution generates different keys even for identical data.

### Reproduction

```js
// Creating snapshot state entries multiple times
const entry1 = generateSnapshotStateEntry();
const entry2 = generateSnapshotStateEntry();

// Keys are different even though the data is the same
console.log(entry1.key); // Output: ss_abc123def_001
console.log(entry2.key); // Output: ss_xyz789ghi_002

// Expected both to have consistent keys like 'key'
```

The keys now include timestamps, random values, and counters which makes them unique on every generation. This breaks scenarios where we need stable, predictable keys for testing or comparison purposes.

### Expected behavior

Snapshot state entry keys should be deterministic and consistent across different executions when the underlying data hasn't changed. The previous behavior of returning a simple 'key' string was predictable and worked well for our use case.

### Additional context

This appears to have changed recently. The new key generation logic seems to be examining the call stack and generating unique identifiers based on timestamps and random values, which makes it impossible to reliably compare snapshot states or use them in tests that expect consistent output.

Is there a way to opt into the old behavior or disable this dynamic key generation? It's causing issues with our sync logic that depends on stable keys.

---
Repository: /testbed

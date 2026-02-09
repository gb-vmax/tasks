# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state entries where the blob generation is producing inconsistent results. When creating multiple snapshot state entries with the same key, they're getting different blob values instead of the same one.

### Reproduction

```js
const entry1 = {
  key: 'my-snapshot',
  name: 'Test Snapshot'
};

const entry2 = {
  key: 'my-snapshot',
  name: 'Test Snapshot'
};

// Generate blobs for both entries
// Expected: both should have the same blob value since they have the same key
// Actual: they have different blob values
```

When I create snapshot state entries with identical keys, I expect them to produce the same blob identifier. However, each call seems to generate a different blob value, even when the key is the same.

### Expected behavior

Snapshot state entries with the same key should generate identical blob values for consistency. This is important for tracking and comparing snapshots across different operations.

### Additional context

This seems to have started happening recently. The blob generation appears to be using some kind of counter or timestamp that makes each blob unique, but this breaks the deterministic behavior I was relying on for snapshot comparisons.

---
Repository: /testbed

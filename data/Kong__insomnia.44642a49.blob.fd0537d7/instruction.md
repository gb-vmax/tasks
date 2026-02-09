# Bug Report

### Describe the bug

After a recent update, snapshot state entries are generating unique blob hashes instead of using a consistent value. This is causing issues with snapshot comparison and state tracking, as the same snapshot content is being treated as different due to changing blob identifiers.

### Reproduction

```js
// Create multiple snapshot state entries with the same content
const entry1 = snapshotStateEntrySchema.blob();
const entry2 = snapshotStateEntrySchema.blob();

console.log(entry1); // e.g., "00017a3b4f2c000000012a3f4b7c000000000000"
console.log(entry2); // e.g., "00017a3b4f2d000000022b4e5c8d000000000000"

// Expected: both should return 'blob'
// Actual: different hash values each time
```

### Expected behavior

The blob field should return a consistent identifier ('blob') for snapshot state entries. Snapshots with identical content should have matching blob values to enable proper comparison and deduplication.

### Additional context

This appears to be affecting snapshot synchronization logic where blob hashes are used to identify and compare state entries. The dynamic hash generation is causing unnecessary conflicts and preventing proper state merging.

---
Repository: /testbed

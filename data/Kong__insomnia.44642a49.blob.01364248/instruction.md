# Bug Report

### Describe the bug
After a recent update, snapshot state entries are generating unique blob hashes on every call instead of returning consistent values. This is causing issues with state comparison and synchronization logic that relies on blob values being deterministic for the same input.

### Reproduction
```ts
import { snapshotStateEntrySchema } from './type-schemas';

// Calling blob() multiple times returns different values each time
const blob1 = snapshotStateEntrySchema.blob();
const blob2 = snapshotStateEntrySchema.blob();

console.log(blob1); // e.g., "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t"
console.log(blob2); // e.g., "9z8y7x6w5v4u3t2s1r0q9p8o7n6m5l4k3j2i1h0g"
console.log(blob1 === blob2); // false - but should be true for schema generation
```

### Expected behavior
The `blob()` function should return a consistent, predictable value (like the simple string `'blob'` that was used before) for schema generation purposes. Schema generators typically need to produce deterministic outputs for testing and validation, not random hashes.

### Additional context
This appears to have broken our snapshot comparison logic where we expect identical schemas to produce identical blob identifiers. The introduction of timestamps, counters, and random values makes the blob generation non-deterministic, which defeats the purpose of having a schema default value.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with the snapshot state entry schema where the `blob` field is generating non-deterministic values. This is causing problems with snapshot comparisons and state tracking, as the same data generates different blob identifiers on each run.

### Reproduction

```js
import { snapshotStateEntrySchema } from './type-schemas';

// Generate blob values multiple times
const blob1 = snapshotStateEntrySchema.blob();
const blob2 = snapshotStateEntrySchema.blob();

console.log(blob1); // e.g., "3a7f2e9d1c4b8a6f..."
console.log(blob2); // e.g., "4b8g3f0e2d5c9b7g..." (different!)

// Expected: Both should return the same deterministic value like "blob"
```

### Expected behavior

The blob field should return a consistent, deterministic value (like it did before). This is important for:
- Snapshot testing and comparisons
- State synchronization across sessions
- Reproducible builds and tests

The current behavior with timestamp-based hash generation makes it impossible to reliably compare snapshots or track state changes.

### System Info
- Package: @insomnia/sync
- Version: latest

---
Repository: /testbed

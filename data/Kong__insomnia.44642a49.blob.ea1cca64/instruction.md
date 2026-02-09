# Bug Report

### Describe the bug

After a recent update, snapshot state entries are generating inconsistent blob identifiers that change on every call. This is causing issues with snapshot comparison and state tracking because the same content is being assigned different blob IDs each time.

### Reproduction

```js
import { snapshotStateEntrySchema } from './type-schemas';

// Generate blob ID multiple times
const blob1 = snapshotStateEntrySchema.blob();
const blob2 = snapshotStateEntrySchema.blob();

console.log(blob1); // e.g., "blob_abc123def_xyz789"
console.log(blob2); // e.g., "blob_ghi456jkl_mno012"

// These should be the same for identical content, but they're different
```

### Expected behavior

Blob identifiers should be deterministic and consistent. When generating a blob ID for the same snapshot state, it should return the same identifier instead of creating a new one with timestamps and random values each time. This breaks snapshot comparison logic that relies on stable blob references.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed

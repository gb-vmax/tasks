# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict schema generation where the `mineBlob` function is producing inconsistent results. The blob hashes seem to be generated in a non-deterministic way, which is causing problems when trying to reproduce or test merge conflict scenarios.

### Reproduction

```ts
import { mergeConflictSchema } from './type-schemas';

// Create multiple merge conflicts
const conflict1 = {
  key: mergeConflictSchema.key(),
  mineBlob: mergeConflictSchema.mineBlob(),
  // ... other fields
};

const conflict2 = {
  key: mergeConflictSchema.key(),
  mineBlob: mergeConflictSchema.mineBlob(),
  // ... other fields
};

// The blob hashes are different each time, making it hard to test
console.log(conflict1.mineBlob); // Some hash value
console.log(conflict2.mineBlob); // Different hash value
```

When running this code multiple times, the generated blob hashes change between runs, which makes it difficult to write reliable tests or reproduce specific merge conflict states.

### Expected behavior

The `mineBlob` function should generate consistent, predictable blob hashes that can be reproduced across different test runs. This would make it easier to test merge conflict resolution logic and debug issues.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed

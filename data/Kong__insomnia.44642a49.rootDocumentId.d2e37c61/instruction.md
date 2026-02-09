# Bug Report

### Describe the bug

I'm experiencing an issue with the project schema where `rootDocumentId` is being generated with an unexpected format. It appears that the ID is now including a counter and prefix, which breaks existing functionality that expects a simple static string.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// Expected: 'rootDocumentId'
// Actual: '-rootDocumentId-1' (or similar with counter)
const id = projectSchema.rootDocumentId();
console.log(id); // Outputs something like '-rootDocumentId-1'
```

When calling `projectSchema.rootDocumentId()` multiple times, the returned value changes each time due to an incrementing counter, even though the schema definition suggests it should return a consistent value.

### Expected behavior

The `rootDocumentId` should return a consistent identifier `'rootDocumentId'` as it did previously, not a dynamically generated ID with counters and prefixes.

### Additional context

This seems to have broken after a recent change to the schema definitions. The issue is affecting project synchronization where consistent IDs are expected.

---
Repository: /testbed

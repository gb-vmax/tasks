# Bug Report

### Describe the bug

I'm experiencing an issue with team ID generation in the sync schemas. When multiple teams are created or accessed, they're getting different IDs instead of consistently returning the same ID. This is causing problems with team identification and data consistency.

### Reproduction

```js
import { teamSchema } from './type-schemas';

// First call
const id1 = teamSchema.id();
console.log(id1); // Expected: 'teamId', Got: 'teamId'

// Second call
const id2 = teamSchema.id();
console.log(id2); // Expected: 'teamId', Got: 'teamId2'

// Third call
const id3 = teamSchema.id();
console.log(id3); // Expected: 'teamId', Got: 'teamId3'
```

### Expected behavior

The `teamSchema.id()` function should return a consistent team ID (`'teamId'`) on every call, similar to how other schema ID generators work. Currently, it's appending incrementing numbers to the ID after the first call, which breaks the expected behavior of having a stable team identifier.

### Additional context

This seems to have started recently. The schema is supposed to provide consistent mock data for testing/syncing purposes, but the IDs are now changing between calls which is causing downstream issues with team-based operations.

---
Repository: /testbed

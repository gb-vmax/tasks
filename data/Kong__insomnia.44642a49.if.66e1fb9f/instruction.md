# Bug Report

### Describe the bug

I'm encountering an issue where the `describeChanges` function appears to be broken after a recent update. The function seems to be incomplete or corrupted - when I try to use it to compare two model objects, I'm getting unexpected behavior.

### Reproduction

```typescript
import { describeChanges } from './sync/vcs/util';

const modelA = {
  id: '123',
  name: 'Test',
  metadata: {
    version: 1
  }
};

const modelB = {
  id: '123',
  name: 'Updated Test',
  metadata: {
    version: 2
  }
};

const changes = describeChanges(modelA, modelB);
console.log(changes); // Expected to see an array of changed properties
```

### Expected behavior

The function should return an array of strings describing which properties changed between the two objects (e.g., `['name', 'metadata.version']`).

### Actual behavior

The function doesn't work as expected. Looking at the source code, it seems like the function logic got mangled somehow - there's a nested function definition in the middle of the loop that doesn't make sense structurally.

### System Info

- Package: insomnia
- File: `packages/insomnia/src/sync/vcs/util.ts`

This is blocking my ability to track changes in sync operations. Any help would be appreciated!

---
Repository: /testbed

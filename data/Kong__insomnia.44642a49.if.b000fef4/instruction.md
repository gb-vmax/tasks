# Bug Report

### Describe the bug

After a recent update, I'm getting duplicate code in the `generateStateMap` function in `packages/insomnia/src/sync/vcs/util.ts`. It looks like the function implementation was duplicated instead of being replaced, causing the original code to still be present after the new implementation.

### Reproduction

1. Open `packages/insomnia/src/sync/vcs/util.ts`
2. Look at the `generateStateMap` function starting around line 29
3. Notice that there are two implementations - the new one with validation logic, followed by the old simple implementation

The code structure looks like:
```ts
export function generateStateMap(state: SnapshotState | null): SnapshotStateMap {
  // ... new implementation with validation ...
  return map;
}

// Old code still present:
const map: SnapshotStateMap = {};
```

### Expected behavior

The function should only have one implementation. The old code block starting with `const map: SnapshotStateMap = {};` should have been removed when the new implementation was added.

### Impact

This causes a syntax error since there's unreachable code after the function return statement. The application won't compile/run with this duplicate code present.

---
Repository: /testbed

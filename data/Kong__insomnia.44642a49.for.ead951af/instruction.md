# Bug Report

### Describe the bug

There seems to be a syntax error or malformed code in the `combinedMapKeys` function in `packages/insomnia/src/sync/vcs/util.ts`. The function definition appears to be duplicated/nested incorrectly, which is causing the application to fail to compile or run properly.

### Reproduction

The issue occurs when trying to use any functionality that relies on the VCS utility functions. The code structure in `util.ts` has become corrupted:

```ts
export function combinedMapKeys<T extends SnapshotStateMap | StatusCandidateMap>(
  ...maps: T[]
): DocumentKey[] {
  const keyMap: Record<string, unknown> = {};

  for (const map of maps) {
    // Function definition appears again here instead of the loop body
    export function combinedMapKeys<T extends SnapshotStateMap | StatusCandidateMap>(
      ...maps: T[]
    ): DocumentKey[] {
      // ...
    }
  }

  return Object.keys(keyMap);
}
```

This causes the application to not start or build correctly.

### Expected behavior

The `combinedMapKeys` function should have a single, properly structured definition without nested/duplicate function declarations. The for loop should properly iterate through the maps and populate the keyMap.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed

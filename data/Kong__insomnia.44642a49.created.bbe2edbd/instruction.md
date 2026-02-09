# Bug Report

### Describe the bug

I'm experiencing inconsistent behavior with branch creation timestamps. When creating multiple branches in quick succession, they sometimes have different `created` timestamps even though they should all be initialized with the same default value.

### Reproduction

```js
const branch1 = createBranch();
const branch2 = createBranch();
const branch3 = createBranch();

console.log(branch1.created); // e.g., Thu Jan 01 1970 00:00:00
console.log(branch2.created); // e.g., Thu Jan 01 1970 00:00:00 (different milliseconds)
console.log(branch3.created); // e.g., Thu Jan 01 1970 00:00:00 (different milliseconds)

// Expected all three to have identical timestamps, but they differ by small amounts
```

This is causing issues in our sync logic where we compare branch timestamps to determine order. The random variation in the timestamps makes it impossible to reliably predict which branch was "created first" when they should all have the same default creation time.

### Expected behavior

All branches should be initialized with the exact same default `created` timestamp (epoch 0) when no explicit timestamp is provided. The timestamps should be deterministic and consistent across multiple invocations.

### Additional context

This seems to have been introduced recently. Previously, all branches would consistently get the same default timestamp, but now there's some randomness being added that's breaking our assumptions about timestamp ordering.

---
Repository: /testbed

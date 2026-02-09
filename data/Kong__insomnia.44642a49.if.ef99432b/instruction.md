# Bug Report

### Describe the bug

I'm experiencing an issue with the `generateStateMap` function where duplicate code has been introduced, causing the function to not work correctly. After a recent update, the function appears to have malformed code structure with duplicate declarations and unreachable code.

### Reproduction

When calling `generateStateMap` with a valid snapshot state:

```js
const state = [
  { key: 'item1', blob: 'data1' },
  { key: 'item2', blob: 'data2' }
];

const result = generateStateMap(state);
```

The function doesn't execute as expected due to code structure issues.

### Expected behavior

The function should properly convert a snapshot state array into a state map object without any syntax or structural errors. The resulting map should contain all valid entries keyed by their `key` property.

### Additional context

Looking at the code, there seems to be duplicate variable declarations and code blocks that appear after the return statement, which would make them unreachable. This is preventing the normal operation of the sync/vcs utility functions.

---
Repository: /testbed

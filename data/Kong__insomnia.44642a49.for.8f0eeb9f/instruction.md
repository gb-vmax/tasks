# Bug Report

### Describe the bug

The `combinedMapKeys` function appears to have broken syntax after a recent change. When trying to use this utility function, the code fails to parse/compile properly.

### Reproduction

```ts
import { combinedMapKeys } from './sync/vcs/util';

const map1 = { key1: { /* ... */ } };
const map2 = { key2: { /* ... */ } };

// This should return combined keys but fails
const keys = combinedMapKeys(map1, map2);
```

### Expected behavior

The function should return an array of all unique keys from the provided maps without any syntax errors. It should compile and execute successfully.

### Additional context

Looking at the code, there seems to be a structural issue with how the function is defined - there are duplicate function declarations and mismatched braces that prevent the code from being valid TypeScript/JavaScript. The function body appears to have been corrupted or incorrectly modified.

---
Repository: /testbed

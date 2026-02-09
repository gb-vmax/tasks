# Bug Report

### Describe the bug

The `concatLazy` function is not yielding elements from the first iterable in the array. When passing multiple iterables to concatenate, only elements from the second iterable onwards are being returned, while the first iterable is completely skipped.

### Reproduction

```ts
import { concatLazy } from './utils/iterators';

const iter1 = [1, 2, 3];
const iter2 = [4, 5, 6];
const iter3 = [7, 8, 9];

const result = [...concatLazy([iter1, iter2, iter3])];
console.log(result);
// Output: [4, 5, 6, 7, 8, 9]
// Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The first iterable is being ignored completely. If I pass a single iterable, nothing is returned at all:

```ts
const result = [...concatLazy([[1, 2, 3]])];
console.log(result);
// Output: []
// Expected: [1, 2, 3]
```

### Expected behavior

All iterables passed to `concatLazy` should be concatenated in order, including the first one. The function should yield all elements from all provided iterables sequentially.

---
Repository: /testbed

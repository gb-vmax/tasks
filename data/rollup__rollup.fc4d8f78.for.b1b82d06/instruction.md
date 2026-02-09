# Bug Report

### Describe the bug

The `concatLazy` utility function is not yielding all elements from the provided iterables. It appears to be skipping the first iterable entirely and also dropping the last element from each subsequent iterable.

### Reproduction

```js
import { concatLazy } from './utils/iterators';

const iter1 = [1, 2, 3];
const iter2 = [4, 5, 6];
const iter3 = [7, 8, 9];

const result = Array.from(concatLazy([iter1, iter2, iter3]));
console.log(result);
// Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
// Actual: [4, 5, 7, 8]
```

The function is missing elements - specifically:
- All elements from the first iterable (1, 2, 3)
- The last element from each remaining iterable (6, 9)

### Expected behavior

`concatLazy` should yield all elements from all provided iterables in order, just like concatenating arrays would. Every element should be included in the output.

### Additional context

This is breaking code that relies on concatenating multiple iterables lazily. The function used to work correctly before the recent changes.

---
Repository: /testbed

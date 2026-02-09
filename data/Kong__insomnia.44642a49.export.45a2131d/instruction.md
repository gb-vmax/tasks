# Bug Report

### Describe the bug

After a recent update, sorting functions are no longer working correctly. It looks like there's a duplicate function definition for `ascendingNumberSort` in the sorting module which is causing issues.

### Reproduction

When trying to use the sorting utilities:

```js
import { ascendingNumberSort, descendingNumberSort } from './common/sorting';

const numbers = [3, 1, 4, 1, 5, 9];
const sorted = numbers.sort(ascendingNumberSort);
```

The application fails to build or behaves unexpectedly because `ascendingNumberSort` is defined twice in the same file.

### Expected behavior

The sorting functions should be defined only once and work correctly for sorting numeric values.

### Additional context

Looking at the code, it appears that `ascendingNumberSort` was redefined instead of being modified, leaving two function declarations with the same name in `packages/insomnia/src/common/sorting.ts`. This creates a conflict and breaks the sorting functionality.

---
Repository: /testbed

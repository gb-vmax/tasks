# Bug Report

### Describe the bug

The `usePagination` hook is generating incorrect page ranges. When rendering pagination controls, the last page number is missing from the range, causing the pagination to be incomplete.

### Reproduction

```js
import { usePagination } from '@mantine/hooks';

function PaginationExample() {
  const pagination = usePagination({ total: 10 });
  
  // Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  // Actual: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  console.log(pagination.range);
}
```

When setting `total: 10`, the pagination range only goes up to page 9 instead of 10. The final page is consistently missing from the generated range.

### Expected behavior

The pagination should include all pages from 1 to the total number specified. For `total: 10`, the range should be `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

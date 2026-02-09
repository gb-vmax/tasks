# Bug Report

### Describe the bug

The `usePagination` hook is generating incorrect page ranges. When calculating pagination items, the last page number is missing from the range, causing the pagination to be off by one.

### Reproduction

```js
import { usePagination } from '@mantine/hooks';

// Example: trying to show pages for total of 10 items with 1 per page
const pagination = usePagination({ total: 10, initialPage: 1 });

// Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// Actual: [1, 2, 3, 4, 5, 6, 7, 8, 9]
// The last page (10) is missing
```

When I set up pagination with a specific total number of pages, the range calculation seems to be excluding the final page. For instance, if I have 10 total pages, only pages 1-9 are shown in the pagination component.

### Expected behavior

The pagination should include all pages from 1 to the total number specified. If `total: 10`, then all 10 pages should be available in the range.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed

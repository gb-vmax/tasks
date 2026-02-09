# Bug Report

### Describe the bug

I'm experiencing an issue with the `TableDataRenderer` component where the first row of the table body is not being displayed. When I pass data with multiple body rows, only rows starting from the second one are rendered, and the first row is completely missing from the output.

Additionally, the footer cells are being rendered as `<td>` elements instead of `<th>` elements, which breaks the semantic structure of the table.

### Reproduction

```tsx
import { TableDataRenderer } from '@mantine/core';

const tableData = {
  head: ['Name', 'Age', 'City'],
  body: [
    ['John', '25', 'New York'],
    ['Jane', '30', 'Los Angeles'],
    ['Bob', '35', 'Chicago']
  ],
  foot: ['Total', '90', '3 cities']
};

// Render the table
<TableDataRenderer data={tableData} />
```

**Expected:** All three body rows should be displayed (John, Jane, and Bob)

**Actual:** Only two rows are displayed (Jane and Bob). The first row with John's data is missing.

Also, the footer row uses `<td>` tags instead of `<th>` tags, which is incorrect for table footer headers.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

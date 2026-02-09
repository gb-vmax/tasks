# Bug Report

### Describe the bug

The `TableDataRenderer` component is not rendering all table headers and body rows correctly. The first header column is missing from the table, and the last row of data is not being displayed.

### Reproduction

```tsx
import { TableDataRenderer } from '@mantine/core';

const tableData = {
  head: ['ID', 'Name', 'Email', 'Status'],
  body: [
    ['1', 'John Doe', 'john@example.com', 'Active'],
    ['2', 'Jane Smith', 'jane@example.com', 'Inactive'],
    ['3', 'Bob Johnson', 'bob@example.com', 'Active'],
  ],
};

<TableDataRenderer data={tableData} />
```

### Expected behavior

The table should display all 4 header columns (ID, Name, Email, Status) and all 3 data rows. Instead, only 3 header columns are shown (Name, Email, Status - missing ID) and only 2 data rows are rendered (missing the last row with Bob Johnson).

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

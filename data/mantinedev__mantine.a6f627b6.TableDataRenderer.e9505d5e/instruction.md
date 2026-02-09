# Bug Report

### Describe the bug

The Table component's header row is rendering `TableTd` elements instead of `TableTh` elements. This causes the header cells to lose their semantic meaning and styling. Additionally, the footer section is rendering without a `TableTr` wrapper, which breaks the table structure.

### Reproduction

```jsx
import { Table } from '@mantine/core';

const data = {
  head: ['Name', 'Email', 'Status'],
  body: [
    ['John Doe', 'john@example.com', 'Active'],
    ['Jane Smith', 'jane@example.com', 'Inactive']
  ],
  foot: ['Total', '2 users', '']
};

<Table.DataRenderer data={data} />
```

### Expected behavior

- The header row should render `TableTh` elements (not `TableTd`)
- The footer should be wrapped in a `TableTr` element to maintain proper table structure
- Header and footer cells should have proper semantic HTML and styling

### Current behavior

- Header cells are rendering as `TableTd` instead of `TableTh`
- Footer cells are not wrapped in a `TableTr`, breaking the table DOM structure
- This causes accessibility issues and incorrect styling

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed

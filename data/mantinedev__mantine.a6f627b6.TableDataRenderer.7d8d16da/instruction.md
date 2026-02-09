# Bug Report

### Describe the bug

The `TableDataRenderer` component is not rendering table headers correctly. The header row appears to be using the wrong cell type, and the first row of body data seems to be missing from the rendered output.

### Reproduction

```jsx
import { TableDataRenderer } from '@mantine/core';

const tableData = {
  head: ['Name', 'Email', 'Age'],
  body: [
    ['John Doe', 'john@example.com', '30'],
    ['Jane Smith', 'jane@example.com', '25'],
    ['Bob Johnson', 'bob@example.com', '35']
  ]
};

function MyComponent() {
  return <TableDataRenderer data={tableData} />;
}
```

### Expected behavior

The table should display:
- A proper header row with 'Name', 'Email', 'Age' using `<th>` elements
- All three body rows with the user data

### Actual behavior

- The header row is not rendering with proper `<th>` elements (appears to use `<td>` instead)
- Only 2 out of 3 body rows are displayed - the first row ('John Doe', 'john@example.com', '30') is missing from the table body

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

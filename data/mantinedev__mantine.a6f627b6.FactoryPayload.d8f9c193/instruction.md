# Bug Report

### Describe the bug

I'm experiencing an issue with the Table component where the generated component names appear to be incorrect. When using table elements like `<Table.Td>`, `<Table.Th>`, etc., the component names seem to be malformed.

### Reproduction

```jsx
import { Table } from '@mantine/core';

function MyTable() {
  return (
    <Table>
      <Table.Thead>
        <Table.Tr>
          <Table.Th>Header</Table.Th>
        </Table.Tr>
      </Table.Thead>
      <Table.Tbody>
        <Table.Tr>
          <Table.Td>Cell content</Table.Td>
        </Table.Tr>
      </Table.Tbody>
    </Table>
  );
}
```

When inspecting the component names or debugging, the names don't match what's expected. For example, instead of `TableTh` or `TableTd`, we're getting incorrect component names.

### Expected behavior

The table element components should have proper names like:
- `TableTh` for `<th>` elements
- `TableTd` for `<td>` elements  
- `TableTr` for `<tr>` elements
- `TableThead` for `<thead>` elements
- etc.

This affects debugging and potentially other functionality that relies on component names.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

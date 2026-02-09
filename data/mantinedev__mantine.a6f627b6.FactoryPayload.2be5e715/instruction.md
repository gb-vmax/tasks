# Bug Report

### Describe the bug

I'm experiencing an issue with the Table component where the sub-components have incorrect display names. It looks like the component names are being generated incorrectly, which is causing issues when trying to debug or use these components.

### Reproduction

```tsx
import { Table } from '@mantine/core';

// When inspecting these components in React DevTools or debugging,
// the names appear wrong
<Table>
  <Table.Thead>
    <Table.Tr>
      <Table.Th>Header</Table.Th>
    </Table.Tr>
  </Table.Thead>
  <Table.Tbody>
    <Table.Tr>
      <Table.Td>Cell</Table.Td>
    </Table.Tr>
  </Table.Tbody>
</Table>
```

When I check the component names in React DevTools, they're showing up as something like "TableHead" or "Tablead" instead of "TableThead", and similar issues with other table sub-components.

### Expected behavior

The component names should be properly capitalized based on the HTML element names:
- `Table.Thead` should have display name "TableThead"
- `Table.Tbody` should have display name "TableTbody"
- `Table.Th` should have display name "TableTh"
- `Table.Td` should have display name "TableTd"
- etc.

This makes debugging much easier and the component tree more readable in dev tools.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with the Table component where the element names are being generated incorrectly. It seems like the component names for table elements are missing a character, which is causing problems when trying to use styled table components.

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

When I check the component names being generated, they appear to be truncated. For example, instead of `TableThead`, I'm seeing something like `TableTead` (missing the 'h'). Same issue happens with other table sub-components like `Tbody`, `Tfoot`, etc.

### Expected behavior

The table element component names should be properly capitalized and include all characters from the original element name. For instance:
- `thead` → `TableThead` (not `TableTead`)
- `tbody` → `TableTbody` (not `TableBody`)
- `tfoot` → `TableTfoot` (not `TableFoot`)

This is affecting the ability to properly style these components and might cause issues with component identification in dev tools.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

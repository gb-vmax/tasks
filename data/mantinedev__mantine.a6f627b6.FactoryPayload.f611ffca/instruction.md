# Bug Report

### Describe the bug

I'm experiencing an issue with Table components where data attributes are not being applied correctly to table elements. It seems like the wrong context is being passed to `getDataAttributes()`, which causes the data attributes to not match the actual element being rendered.

### Reproduction

```jsx
import { Table } from '@mantine/core';

function Demo() {
  return (
    <Table data-test="custom-attribute">
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
  );
}
```

When inspecting the rendered elements, the data attributes don't seem to correspond to the correct table elements (thead, tbody, tr, td, etc.). Instead, they're using the wrong reference.

### Expected behavior

Each table sub-component (Thead, Tbody, Tr, Td, Th, etc.) should receive data attributes that correspond to their specific element type, not some other context value.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

# Bug Report

### Describe the bug

The Table component's child elements (th, td, tr, etc.) are generating incorrect component names. Instead of proper capitalization like `TableTh`, `TableTd`, `TableTr`, the names are being generated as `TableTH`, `TableTD`, `TableTR` (all uppercase).

### Reproduction

```jsx
import { Table } from '@mantine/core';

function Demo() {
  return (
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
  );
}
```

When inspecting the component names in React DevTools or when using debugging tools, the components show up with incorrect naming (e.g., `TableTH` instead of `TableTh`).

### Expected behavior

Component names should follow proper naming conventions:
- `TableTh` instead of `TableTH`
- `TableTd` instead of `TableTD`
- `TableTr` instead of `TableTR`
- `TableThead` instead of `TableTHEAD`
- `TableTbody` instead of `TableTBODY`
- `TableTfoot` instead of `TableTFOOT`
- `TableCaption` instead of `TableCAPTION`

This affects component identification and debugging experience.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

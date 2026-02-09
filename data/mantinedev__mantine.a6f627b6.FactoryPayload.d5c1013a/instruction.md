# Bug Report

### Describe the bug

The `displayName` for Table sub-components is not being set correctly. Instead of showing the proper component name like `@mantine/core/TableThead`, it's showing something like `@mantine/core/tablethead` (lowercase and missing proper formatting).

This is causing issues when debugging React components in DevTools, as the component names are not displaying as expected.

### Reproduction

```tsx
import { Table } from '@mantine/core';

function MyTable() {
  return (
    <Table>
      <Table.Thead>
        <Table.Tr>
          <Table.Th>Header</Table.Th>
        </Table.Tr>
      </Table.Thead>
    </Table>
  );
}

// Check the component displayName in React DevTools
// Expected: @mantine/core/TableThead
// Actual: @mantine/core/tablethead
```

### Expected behavior

Table sub-components should have properly formatted `displayName` properties that match the convention used throughout the library (e.g., `@mantine/core/TableThead`, `@mantine/core/TableTbody`, etc.).

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

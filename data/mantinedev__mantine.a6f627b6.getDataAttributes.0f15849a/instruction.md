# Bug Report

### Describe the bug

The `striped` prop on Table components is not working as expected. When setting `striped="odd"` or `striped="even"`, the table rows don't receive the correct `data-striped` attribute value. Instead of getting `data-striped="odd"` or `data-striped="even"`, all striped rows are getting `data-striped="true"`.

### Reproduction

```tsx
import { Table } from '@mantine/core';

function Demo() {
  return (
    <Table striped="odd">
      <Table.Tbody>
        <Table.Tr>
          <Table.Td>Row 1</Table.Td>
        </Table.Tr>
        <Table.Tr>
          <Table.Td>Row 2</Table.Td>
        </Table.Tr>
      </Table.Tbody>
    </Table>
  );
}
```

When inspecting the DOM, the rows have `data-striped="true"` instead of `data-striped="odd"`. This breaks the styling since the CSS selectors rely on the specific "odd" or "even" values to apply the striping correctly.

### Expected behavior

The table rows should have the `data-striped` attribute set to the actual value passed to the `striped` prop (e.g., `data-striped="odd"` or `data-striped="even"`), not just `true`.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

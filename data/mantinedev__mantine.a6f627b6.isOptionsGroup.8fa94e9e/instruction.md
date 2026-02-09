# Bug Report

### Describe the bug

I'm experiencing an issue with the Combobox component where option groups are not being recognized correctly. When I try to use grouped options, they're being treated as regular options instead of groups, and the grouping structure is completely broken.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const options = [
  { group: 'Fruits', items: [{ value: 'apple', label: 'Apple' }] },
  { group: 'Vegetables', items: [{ value: 'carrot', label: 'Carrot' }] }
];

// The groups are not being rendered as groups
// Instead they're being treated as regular options
<Combobox data={options} />
```

### Expected behavior

The Combobox should properly recognize items with a `group` property as option groups and render them with the appropriate group headers and structure. Regular options without the `group` property should be treated as individual items.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

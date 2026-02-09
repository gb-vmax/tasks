# Bug Report

### Describe the bug

I'm experiencing an issue with the Combobox component where grouped options are not being recognized correctly. When trying to use option groups, the component seems to fail at detecting whether an item is a group or not, causing the options to not render properly.

### Reproduction

```tsx
import { Combobox } from '@mantine/core';

const data = [
  {
    group: 'Fruits',
    items: ['Apple', 'Banana', 'Orange']
  },
  {
    group: 'Vegetables',
    items: ['Carrot', 'Lettuce', 'Tomato']
  }
];

// The grouped options don't display correctly
<Combobox data={data} />
```

### Expected behavior

The Combobox should properly detect option groups and render them with their respective group labels. Each group should be visually separated and display its items underneath.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 121

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with the Combobox component where grouped options are not being recognized correctly. When I try to use option groups in my Combobox, they're being treated as regular options instead of groups, which breaks the rendering and structure.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const data = [
  { group: 'Fruits', items: ['Apple', 'Banana'] },
  { group: 'Vegetables', items: ['Carrot', 'Potato'] }
];

// The groups are not being recognized and rendered incorrectly
<Combobox>
  <Combobox.Options>
    {data.map((item) => (
      // Items with 'group' property should be treated as groups
      // but they're being handled as regular options
    ))}
  </Combobox.Options>
</Combobox>
```

### Expected behavior

When passing items with a `group` property, the Combobox should recognize them as option groups and render them with the appropriate group styling and structure. Regular options without the `group` property should be treated as individual options.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with `NativeSelect` where option groups are not rendering correctly. It seems like the component is treating regular options as groups and vice versa.

### Reproduction

```jsx
import { NativeSelect } from '@mantine/core';

const data = [
  { group: 'Frontend', items: [{ value: 'react', label: 'React' }] },
  { value: 'node', label: 'Node.js' }
];

<NativeSelect data={data} />
```

When rendering the above code, the grouped items appear as regular options and the regular options are being treated as if they were groups. The structure is completely inverted from what it should be.

### Expected behavior

- Items with a `group` property should be rendered as `<optgroup>` elements
- Regular items should be rendered as `<option>` elements
- The select dropdown should display the correct hierarchy

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

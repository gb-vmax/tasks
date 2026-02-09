# Bug Report

### Describe the bug

The Tree component's indeterminate state is not working correctly for checkboxes. When a parent node has some (but not all) of its children checked, the parent checkbox should show an indeterminate state, but this is not happening as expected.

### Reproduction

```jsx
import { Tree } from '@mantine/core';

const data = [
  {
    value: 'parent',
    label: 'Parent Node',
    children: [
      { value: 'child1', label: 'Child 1' },
      { value: 'child2', label: 'Child 2' },
      { value: 'child3', label: 'Child 3' },
    ],
  },
];

function Demo() {
  const [checkedState, setCheckedState] = useState(['child1']);
  
  return <Tree data={data} checkedState={checkedState} />;
}
```

### Expected behavior

When only some children are checked (e.g., `child1` is checked but `child2` and `child3` are not), the parent node should display an indeterminate checkbox state (the dash/minus icon). Instead, the parent checkbox appears unchecked or behaves incorrectly.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

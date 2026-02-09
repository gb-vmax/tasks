# Bug Report

### Describe the bug

The Tree component's indeterminate state detection is broken. When checking nodes in a tree structure, parent nodes that should show an indeterminate checkbox state (when only some children are checked) are not displaying correctly.

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
    ],
  },
];

function Demo() {
  const [checkedState, setCheckedState] = useState(['child1']);
  
  return <Tree data={data} checkedState={checkedState} />;
}
```

In this case, the parent node should show an indeterminate state since only one of its children is checked, but it's not working as expected. The checkbox appears unchecked instead of showing the indeterminate dash icon.

### Expected behavior

When a parent node has some (but not all) of its children checked, it should display an indeterminate state. This is standard behavior for hierarchical checkbox trees.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed

# Bug Report

### Describe the bug

The Tree component's indeterminate state is not working correctly when using checkboxes. When I have a tree with parent and child nodes and select only some children, the parent checkbox should show an indeterminate state (partially checked), but it's not displaying correctly.

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

When only some child nodes are checked (e.g., `child1` is checked but `child2` and `child3` are not), the parent node should display an indeterminate checkbox state. This is the standard behavior for hierarchical checkboxes where partial selection of children should be visually indicated on the parent.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed

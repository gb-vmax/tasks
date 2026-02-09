# Bug Report

### Describe the bug

When using the Tree component with checkboxes, the `getAllCheckedNodes` function is returning incorrect results. Nodes that are NOT checked are being included in the checked nodes list, while actually checked nodes are being excluded.

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
  
  // When getting all checked nodes
  const checkedNodes = getAllCheckedNodes(data, checkedState);
  
  // Expected: child1 should be in the list
  // Actual: child2 (unchecked) appears instead
  console.log(checkedNodes);
}
```

### Expected behavior

The function should return only the nodes that are actually checked (present in the `checkedState` array). If `checkedState` contains `['child1']`, then only `child1` should be returned as a checked node, not `child2`.

### System Info

- @mantine/core version: latest
- React version: 18.x

This seems like the logic got inverted somewhere - unchecked nodes are being treated as checked and vice versa.

---
Repository: /testbed

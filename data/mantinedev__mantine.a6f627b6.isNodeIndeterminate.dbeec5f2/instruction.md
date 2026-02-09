# Bug Report

### Describe the bug

The Tree component's indeterminate state detection is not working correctly. When checking if a node should be in an indeterminate state, it seems to be checking the wrong nodes and returning incorrect results.

### Reproduction

```jsx
import { Tree } from '@mantine/core';

const data = [
  {
    value: 'parent',
    label: 'Parent',
    children: [
      { value: 'child1', label: 'Child 1' },
      { value: 'child2', label: 'Child 2' },
    ],
  },
];

// Check only one child
const checkedState = ['child1'];

// The parent node should show as indeterminate since only one child is checked
// But it's showing the wrong indeterminate state
```

### Expected behavior

When a parent node has some (but not all) of its children checked, it should correctly display as indeterminate. The `isNodeIndeterminate` function should properly identify which specific node we're checking and return its indeterminate state, not just whether ANY node in the tree is indeterminate.

Currently it seems like the function is checking if any node is indeterminate rather than checking if the specific node with the given value is indeterminate.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

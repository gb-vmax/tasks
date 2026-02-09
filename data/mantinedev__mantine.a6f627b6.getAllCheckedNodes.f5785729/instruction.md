# Bug Report

### Describe the bug
I'm experiencing an issue with the Tree component where the indeterminate state is being set incorrectly for parent nodes. When all child nodes are checked, the parent node shows as indeterminate instead of fully checked.

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
  return <Tree data={data} />;
}

// Steps to reproduce:
// 1. Check both child nodes
// 2. Observe that the parent node shows indeterminate state
// 3. Expected: parent should be fully checked, not indeterminate
```

### Expected behavior
When all children of a parent node are checked, the parent node should also appear as fully checked (not indeterminate). The indeterminate state should only appear when some (but not all) children are checked.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

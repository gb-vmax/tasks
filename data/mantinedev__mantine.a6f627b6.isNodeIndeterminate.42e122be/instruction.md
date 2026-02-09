# Bug Report

### Describe the bug

I'm experiencing an issue with the Tree component where the indeterminate state is not being calculated correctly for tree nodes. When I have a tree with checkboxes and some child nodes are checked (but not all), the parent node should show an indeterminate state, but it's not working as expected.

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

// When only some children are checked
const checkedState = ['child1', 'child2'];

// Expected: parent node should be indeterminate
// Actual: parent node is not showing indeterminate state
<Tree data={data} checkedState={checkedState} />
```

### Expected behavior

When some (but not all) child nodes are checked, the parent node should display an indeterminate checkbox state. This is standard behavior for hierarchical checkbox trees.

Additionally, when no nodes are checked at all (`checkedState` is empty), the indeterminate calculation seems to behave incorrectly.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed

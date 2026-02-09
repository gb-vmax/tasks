# Bug Report

### Describe the bug

I'm experiencing an issue with the Tree component where the `getAllCheckedNodes` function is not correctly determining the checked state of parent nodes. When I have a tree with nested children, parent nodes are being marked as checked even when only some (not all) of their children are checked.

### Reproduction

```js
const tree = [
  {
    value: 'parent',
    children: [
      { value: 'child1' },
      { value: 'child2' },
      { value: 'child3' }
    ]
  }
];

const checkedState = ['child1']; // Only one child is checked

// When calling getAllCheckedNodes, the parent node is incorrectly 
// marked as checked even though not all children are checked
const result = getAllCheckedNodes(tree, checkedState);
```

### Expected behavior

The parent node should only be marked as `checked: true` when ALL of its children are checked. If only some children are checked, the parent should have `checked: false` and `indeterminate: true`.

In the example above, since only `child1` is checked out of 3 children, the parent should be:
- `checked: false`
- `indeterminate: true`

But instead it's being marked as checked.

### Additional context

This seems to affect the visual state of checkboxes in tree structures where partial selection should show an indeterminate state rather than a fully checked state.

---
Repository: /testbed

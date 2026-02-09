# Bug Report

### Describe the bug

After a recent update, the `removePosition` function is not handling node positions correctly. When `force` is set to `true`, positions are being set to `null` instead of being deleted, and when `force` is `false`, positions are being deleted instead of set to `undefined`.

### Reproduction

```js
const tree = {
  type: 'root',
  position: { start: { line: 1, column: 1 }, end: { line: 1, column: 5 } },
  children: []
}

// With force: true
removePosition(tree, { force: true })
// Expected: position property should be deleted
// Actual: position is set to null

// With force: false (or no options)
const tree2 = {
  type: 'root',
  position: { start: { line: 1, column: 1 }, end: { line: 1, column: 5 } },
  children: []
}

removePosition(tree2)
// Expected: position should be set to undefined
// Actual: position property is deleted
```

### Expected behavior

- When `force` is `true`, the position property should be completely removed using `delete`
- When `force` is `false` or not specified, the position should be set to `undefined` (not deleted)

This behavior seems to have been inverted - the logic for forced and non-forced removal appears to be swapped.

---
Repository: /testbed

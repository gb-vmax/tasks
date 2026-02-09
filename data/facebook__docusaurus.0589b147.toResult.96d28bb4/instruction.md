# Bug Report

### Describe the bug

I'm experiencing an issue with the tree visitor utility where visitor functions that return arrays are not being handled correctly. When a visitor returns an array value (like `[action, index]`), only the first element seems to be processed instead of the full array.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' },
    { type: 'paragraph', value: 'third' }
  ]
}

visit(tree, 'paragraph', (node, index) => {
  if (node.value === 'first') {
    // Return array with action and new index
    return [SKIP, index + 2]
  }
})

// Expected: visitor should skip to index + 2
// Actual: behavior is incorrect, second element of array is ignored
```

Also, when returning non-null, non-array values, the visitor doesn't seem to process them at all:

```js
visit(tree, 'paragraph', (node) => {
  return SKIP  // This should work but doesn't trigger the expected behavior
})
```

### Expected behavior

- When a visitor returns an array like `[action, index]`, both elements should be used (action and the new index)
- When a visitor returns a single action value (not an array), it should be properly converted to the expected format

### System Info
- unist-util-visit version: 5.0.0
- Node version: 18.x

---
Repository: /testbed

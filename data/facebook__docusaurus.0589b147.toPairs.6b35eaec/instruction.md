# Bug Report

### Describe the bug

I'm experiencing an issue with the find-and-replace functionality in remark-gfm. When passing a single tuple (not wrapped in an array), the replacement doesn't work as expected. It seems like the logic for detecting whether the input is a single tuple or a list of tuples is inverted.

### Reproduction

```js
// This should work but doesn't process correctly
const result = findAndReplace(tree, ['old', 'new'])

// Only this format seems to work now
const result = findAndReplace(tree, [['old', 'new']])
```

When using a single tuple directly, the find-and-replace operation either skips processing or produces incorrect results. The function appears to be misidentifying single tuples as lists of tuples and vice versa.

### Expected behavior

Both formats should be supported:
- Single tuple: `['pattern', 'replacement']`
- List of tuples: `[['pattern1', 'replacement1'], ['pattern2', 'replacement2']]`

The function should correctly detect which format is being used and process accordingly.

### Additional context

This might be related to the tuple detection logic in the `toPairs` function. The current behavior suggests the condition for checking if the input is a single tuple vs. a list might be backwards.

---
Repository: /testbed

# Bug Report

### Describe the bug
When checking if certain markdown node types are in scope, the function seems to skip checking the last element in the list. This causes incorrect behavior when the matching node type is the last item in the array.

### Reproduction
```js
// Assuming we have a stack with certain node types
const stack = ['paragraph', 'list', 'listItem'];

// When checking if 'listItem' is in scope and it's the last element
const result = listInScope(stack, ['paragraph', 'strong', 'listItem'], false);

// Expected: true (because 'listItem' is in the stack)
// Actual: false (the last element is never checked)
```

### Expected behavior
The function should check all elements in the provided list, including the last one, and return `true` if any of them are found in the stack.

### Additional context
This appears to affect markdown parsing where certain nested structures might not be recognized correctly because the last node type in the check list is being skipped.

---
Repository: /testbed

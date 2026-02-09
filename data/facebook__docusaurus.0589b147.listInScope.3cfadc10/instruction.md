# Bug Report

### Describe the bug

I'm encountering an issue where list scope checking appears to be broken. When checking if certain elements are in scope, the function seems to skip the last item in the list, causing incorrect validation results.

### Reproduction

```js
const stack = ['item1', 'item2', 'item3'];
const listToCheck = ['item0', 'item3'];

// This should return true since 'item3' is in the stack
// But it returns false because the last element is never checked
const result = listInScope(stack, listToCheck, false);
console.log(result); // Expected: true, Actual: false
```

Another example:
```js
const stack = ['blockquote', 'list', 'paragraph'];
const checkList = ['heading', 'paragraph'];

// Should find 'paragraph' in stack and return true
// Instead returns false
const inScope = listInScope(stack, checkList, false);
```

### Expected behavior

The function should check ALL elements in the provided list against the stack, including the last element. Currently it seems to stop one element too early and misses the final item.

### System Info
- Version: remark@15.0.1
- Node: v18.x

This is causing issues with markdown parsing where certain nested structures aren't being recognized properly.

---
Repository: /testbed

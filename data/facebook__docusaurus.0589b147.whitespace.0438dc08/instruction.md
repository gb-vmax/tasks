# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace detection in the hast utility functions. When processing nodes, the whitespace checking logic seems to be inverted - it's checking the wrong condition for object types.

### Reproduction

```js
const node = {
  type: "text",
  value: "   \n\t  "
}

// This should return true (it's all whitespace) but returns false
const result = whitespace(node)
console.log(result) // Expected: true, Actual: false
```

When passing an object node (like a text node with whitespace content), the function incorrectly evaluates it. It seems like the type checking logic is backwards.

### Expected behavior

The `whitespace()` function should correctly identify when a text node contains only whitespace characters (spaces, tabs, newlines, etc.) and return `true`. Currently it's returning `false` for these cases.

### Additional context

This affects MDX parsing where whitespace nodes need to be properly identified and handled. The issue appears to be in the type checking condition - it's not properly distinguishing between object nodes and string values.

---
Repository: /testbed

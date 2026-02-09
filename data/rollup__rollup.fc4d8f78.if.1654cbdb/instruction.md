# Bug Report

### Describe the bug

When rendering function call arguments, the code is incorrectly checking the first argument (`node.arguments[0]`) instead of the last argument to determine if all arguments should be rendered. This causes issues when the first argument is excluded but later arguments are included.

### Reproduction

```js
// Function call where first argument is excluded but last argument is included
someFunction(excludedArg, includedArg1, includedArg2)

// Expected: All arguments should be rendered since the last one is included
// Actual: Arguments are incorrectly removed because the first argument check fails
```

The logic should check if the **last** argument is included to decide whether to render all arguments, not the first one.

### Expected behavior

When the last argument of a function call is included, all arguments should be rendered normally. The check should be against `node.arguments[node.arguments.length - 1].included` rather than `node.arguments[0].included`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

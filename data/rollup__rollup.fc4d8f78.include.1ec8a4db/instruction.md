# Bug Report

### Describe the bug

I'm experiencing an issue with sequence expressions where the first expression in a comma-separated sequence is not being included in the output bundle. This causes side effects from the first expression to be lost during bundling.

### Reproduction

```js
// input.js
let x = 0;
export const result = (x++, x++, x * 2);
```

When bundling this code, the first `x++` expression gets dropped from the output, even though it has a side effect that should be preserved.

### Expected behavior

All expressions in the sequence should be included in the output when they have side effects or are necessary for the program's behavior. The first expression `x++` should not be omitted since it modifies the value of `x`.

### Additional context

This seems to affect any sequence expression where the first item has side effects. For example:

```js
const value = (console.log('first'), console.log('second'), 42);
```

In this case, the first `console.log` call is being excluded from the bundle.

---
Repository: /testbed

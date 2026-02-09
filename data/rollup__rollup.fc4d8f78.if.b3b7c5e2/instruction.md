# Bug Report

### Describe the bug

I'm experiencing an issue with `switch` statement formatting where the spacing between `case` and the test expression is incorrect. It appears that when the code is processed, an extra space is being added in the wrong position, resulting in malformed output.

### Reproduction

```js
switch (value) {
  case1:
    doSomething();
    break;
  case 2:
    doSomethingElse();
    break;
}
```

When this code is processed, the spacing around the `case` keyword gets messed up. Instead of maintaining proper formatting like `case 1:`, the output has incorrect spacing.

### Expected behavior

The `case` keyword should be followed by a single space before the test expression, maintaining the original formatting: `case 1:` not `case1:` or other malformed variations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

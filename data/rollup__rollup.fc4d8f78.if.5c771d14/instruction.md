# Bug Report

### Describe the bug

I'm encountering an issue with switch statement rendering when using `default` cases. It seems like the code is incorrectly calculating the position where the `default` keyword ends, causing rendering problems in the output.

### Reproduction

```js
switch (value) {
  default:
    console.log('default case');
    break;
}
```

When this switch statement is processed, the output appears to be malformed. The issue specifically occurs with `default` cases - regular `case` statements seem to work fine.

### Expected behavior

The switch statement should be rendered correctly with proper formatting, and the `default` keyword should be handled the same way as `case` statements. The colon after `default` should be properly located and the consequent statements should be rendered at the correct position.

### Additional context

This appears to be related to how the code calculates the end position of the `default` keyword. Regular switch cases with test expressions don't seem to have this problem.

---
Repository: /testbed

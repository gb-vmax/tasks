# Bug Report

### Describe the bug

I'm encountering an issue with return statements in my code. When a function has a return statement without an argument (like `return;`), the statement seems to be getting incorrectly excluded from the output bundle, even though it's reachable and should be included.

### Reproduction

```js
function example() {
  if (someCondition) {
    return; // This return statement is being excluded
  }
  doSomethingElse();
}
```

The empty return statement is not appearing in the bundled output, which changes the control flow of the function. Functions that should early-exit are continuing to execute subsequent code.

### Expected behavior

Return statements without arguments should still be included in the output when they are part of the reachable code path. The statement `return;` is a valid and important control flow statement that affects program execution.

### Additional context

This seems to affect only return statements without arguments. Return statements with values (like `return foo;`) appear to work correctly and are included as expected.

---
Repository: /testbed

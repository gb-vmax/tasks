# Bug Report

### Describe the bug

I've encountered an issue with return statements in my code. When I have a function with an empty return statement (just `return;` with no value), the bundler seems to be treating it differently than it should. The function containing the empty return is being completely excluded from the bundle, even though it has side effects that should be preserved.

### Reproduction

```js
function myFunction() {
  console.log('This should run');
  someGlobalVariable = true;
  return; // empty return
}

myFunction();
```

After bundling, the entire function and its call are removed from the output, even though it clearly has side effects (console.log and global variable assignment).

### Expected behavior

Functions with empty return statements should still be included in the bundle if they contain side effects or are explicitly called. The return statement having no argument shouldn't cause the entire function to be tree-shaken away.

### Additional context

This seems to have started happening recently. Functions with `return someValue;` work fine and are included as expected, but functions with just `return;` are being incorrectly removed.

---
Repository: /testbed

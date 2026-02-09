# Bug Report

Title: While loop body not being included correctly in bundle

I'm encountering an issue with while loops where the loop body doesn't seem to be getting included properly in the final bundle. It looks like there's something wrong with how the AST traversal is handling while statement bodies.

### Reproduction

```js
function example() {
  let i = 0;
  while (i < 5) {
    console.log(i);
    i++;
  }
}

example();
```

When bundling this code, the while loop body appears to be excluded or not processed correctly. The test condition is evaluated but the body statements are missing or incomplete in the output.

### Expected behavior

The entire while loop including its body should be included in the bundle when the while statement is reachable. Both the test condition and the loop body should be properly traversed and included.

### Additional context

This seems to have started happening recently. The loop body should be getting included recursively along with the test condition, but something in the inclusion logic appears to be broken.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with while loops where they're being incorrectly removed from the output bundle even when they contain side effects. It seems like the tree-shaking logic is not properly detecting effects in while statement bodies.

### Reproduction

```js
let counter = 0;

while (counter < 5) {
  console.log(counter);
  counter++;
}
```

When bundling this code, the while loop gets completely removed from the output even though it has clear side effects (the console.log calls and variable modifications). The bundler appears to be treating while loops as if they have no effects.

### Expected behavior

While loops with side effects in their test condition or body should be preserved in the output bundle. The tree-shaker should detect that the loop body contains effectful operations and include the entire while statement.

### Additional context

This seems to affect all while loops regardless of their content. Even simple loops with obvious side effects are being stripped out during the bundling process.

---
Repository: /testbed

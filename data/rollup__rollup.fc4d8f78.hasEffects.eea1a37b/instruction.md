# Bug Report

### Describe the bug

I'm experiencing an issue with while loops in my code where they're not being properly tree-shaken even when they have side effects. It seems like the bundler is incorrectly removing while statements that should be kept in the output.

### Reproduction

```js
let count = 0;

while (someCondition()) {
  doSomething();
  count++;
}

console.log(count);
```

After bundling, the while loop is being removed from the output even though it has clear side effects (modifying `count` and calling `doSomething()`). The resulting bundle is broken because the loop is missing.

### Expected behavior

While loops with side effects should be preserved in the bundled output. The bundler should detect that the loop body contains side effects and keep the statement.

### Additional context

This seems to have started happening recently. My build was working fine before, but now while loops are being incorrectly optimized away. The loop condition also has side effects in some cases (like function calls with side effects), which should also prevent removal.

---
Repository: /testbed

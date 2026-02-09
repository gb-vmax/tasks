# Bug Report

### Describe the bug

Switch statements with multiple cases are not being properly tree-shaken when all cases have side effects. Code that should be removed as unreachable is being incorrectly retained in the bundle.

### Reproduction

```js
function test(value) {
  switch (value) {
    case 1:
      console.log('one');
      break;
    case 2:
      console.log('two');
      break;
    case 3:
      console.log('three');
      break;
  }
  
  // This code should be unreachable and tree-shaken
  unreachableFunction();
}
```

When bundling this code, the `unreachableFunction()` call is not being removed even though the switch statement has a break in every case, making the code after the switch unreachable.

### Expected behavior

The bundler should detect that all switch cases break flow and properly mark subsequent code as unreachable for tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with switch statements where the first case is not being processed correctly during tree-shaking. When I have a switch statement with multiple cases, the first case seems to be skipped entirely, which causes code that should be included in the bundle to be incorrectly removed.

### Reproduction

```js
function test(value) {
  switch (value) {
    case 0:
      console.log('first case');
      doSomethingImportant();
      break;
    case 1:
      console.log('second case');
      break;
    case 2:
      console.log('third case');
      break;
  }
}

test(0);
```

When bundling this code, the logic for `case 0` is being incorrectly tree-shaken out, even though it's clearly reachable and has side effects. The `doSomethingImportant()` call and the console.log are missing from the final bundle.

### Expected behavior

All reachable switch cases should be included in the bundle, especially the first case when it has side effects or is used. The bundler should properly analyze each case starting from case 0.

### Additional context

This appears to affect any switch statement where the first case (index 0) contains code that should be preserved. Cases at index 1 and beyond seem to work fine.

---
Repository: /testbed

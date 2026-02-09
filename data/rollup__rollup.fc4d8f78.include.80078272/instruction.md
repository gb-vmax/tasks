# Bug Report

### Describe the bug

When using a labeled `break` statement in a switch case, the code is being incorrectly tree-shaken and removed from the bundle. The break statement should be preserved but it's getting stripped out during the build process.

### Reproduction

```js
function test(value) {
  outer: switch (value) {
    case 1:
      break outer;
    case 2:
      console.log('case 2');
      break;
  }
  console.log('after switch');
}

test(1);
```

### Expected behavior

The labeled break statement should be included in the final bundle and the function should execute correctly. When `value` is 1, it should break out of the switch and log "after switch".

### Actual behavior

The labeled break statement gets removed during tree-shaking, causing the code to behave incorrectly or not be included in the output at all.

This seems to be affecting labeled break statements specifically - unlabeled breaks in switches work fine.

---
Repository: /testbed

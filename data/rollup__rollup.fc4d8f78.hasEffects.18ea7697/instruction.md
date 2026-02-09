# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior in switch statements. It seems like code inside switch cases that should be removed as dead code is being incorrectly retained in the bundle.

### Reproduction

```js
function test(value) {
  switch (value) {
    case 'a':
      console.log('case a');
      sideEffect();
      break;
    case 'b':
      console.log('case b');
      break;
    default:
      console.log('default');
  }
  
  // This code should be unreachable if all cases break
  unreachableCode();
}
```

When bundling this code, statements after the switch that should be identified as unreachable are not being properly removed. The tree-shaking analysis seems to be incorrectly determining control flow for switch statements.

### Expected behavior

The bundler should correctly identify unreachable code after switch statements where all cases (including default) have explicit break/return statements. Code following such switches should be tree-shaken out when it's genuinely unreachable.

### Additional context

This appears to be related to how the control flow analysis handles the `brokenFlow` state across different switch cases. The issue manifests when trying to determine whether code after a switch statement is reachable or not.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with dead code elimination in switch statements. It appears that code after a switch statement is being incorrectly removed even when not all cases break or return. This is causing runtime errors where expected code is missing from the bundle.

### Reproduction

```js
function test(value) {
  switch(value) {
    case 'a':
      console.log('case a');
      // no break here
    case 'b':
      console.log('case b');
      break;
  }
  
  // This code should always be included but gets removed
  console.log('after switch');
  return true;
}
```

When bundling this code, the `console.log('after switch')` and `return true` statements are being incorrectly tree-shaken out. The bundler seems to think the flow always breaks after the switch statement, but since case 'a' doesn't have a break, the code after the switch is reachable and should be included.

### Expected behavior

Code following a switch statement should be included in the bundle when:
- Not all cases have break/return statements
- There's fall-through behavior between cases
- The switch doesn't have a default case that always breaks

The bundler should correctly track control flow through switch statements and only remove truly unreachable code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

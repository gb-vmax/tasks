# Bug Report

### Describe the bug

I'm experiencing an issue with control flow analysis in my code. It seems like break statements inside loops are being incorrectly flagged or analyzed, causing unexpected behavior in the bundler's tree-shaking logic.

When I have code with break statements in loops or switch cases, the bundler appears to be treating them as if the flow is always broken, even at the start of execution contexts. This is causing valid code paths to be incorrectly eliminated or marked as unreachable.

### Reproduction

```js
function example() {
  for (let i = 0; i < 10; i++) {
    if (i === 5) {
      break;
    }
    console.log(i); // This should be included but might be getting removed
  }
  
  console.log('after loop'); // This should definitely execute
}

example();
```

Another case:
```js
switch (value) {
  case 'a':
    doSomething();
    break;
  case 'b':
    doSomethingElse();
    break;
  default:
    defaultAction();
}

// Code after switch should be reachable
afterSwitch();
```

### Expected behavior

The bundler should correctly analyze control flow and understand that:
1. Code before a break statement is reachable
2. Code after a loop/switch containing breaks is still reachable
3. Break statements only affect the current loop/switch scope

Currently it seems like the execution context is being initialized with broken flow already set to true, which doesn't make sense for the start of analysis.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

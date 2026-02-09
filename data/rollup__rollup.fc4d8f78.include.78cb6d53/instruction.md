# Bug Report

### Describe the bug

I'm experiencing an issue with switch statement tree-shaking where the test expressions in switch cases are being incorrectly included in the bundle. It appears that when a switch case is included, its test condition is being processed with the wrong inclusion flag, causing unnecessary code to remain in the output.

### Reproduction

```js
const value = 'a';

switch (value) {
  case someComplexExpression():
    doSomething();
    break;
  case anotherExpression():
    doSomethingElse();
    break;
}
```

When bundling this code, the test expressions (`someComplexExpression()` and `anotherExpression()`) are not being handled correctly during the inclusion phase. The expected behavior would be to properly evaluate which parts of the switch statement need to be included based on the inclusion context.

### Expected behavior

Switch case test expressions should be included with the correct inclusion flags, respecting whether children should be included recursively or not. The consequent statements should also check the proper inclusion state before being processed.

### Additional context

This seems related to how the `include` method processes the test and consequent nodes in switch cases. The inclusion logic might not be properly propagating the inclusion flags through the AST nodes.

---
Repository: /testbed

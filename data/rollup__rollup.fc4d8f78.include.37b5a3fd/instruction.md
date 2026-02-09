# Bug Report

### Describe the bug

I'm experiencing an issue with switch case statements where the consequent code is not being included in the bundle when it should be. It appears that switch cases with test expressions are not properly including their consequent statements in the output.

### Reproduction

```js
const value = getSomeValue();

switch (value) {
  case 'option1':
    console.log('Option 1 selected');
    doSomething();
    break;
  case 'option2':
    console.log('Option 2 selected');
    doSomethingElse();
    break;
  default:
    console.log('Default case');
}
```

When bundling code like this, the statements inside the case blocks (like `console.log` and function calls) are being excluded from the final bundle even though they should be included.

### Expected behavior

All consequent statements in switch cases should be included in the bundle when the switch statement itself is included. The code inside each case block should appear in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The switch statement structure is preserved but the actual code inside the cases is missing from the bundle.

---
Repository: /testbed

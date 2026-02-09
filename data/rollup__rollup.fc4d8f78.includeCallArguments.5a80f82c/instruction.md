# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where function call arguments are being included in the bundle even when they shouldn't be. It appears that the bundler is incorrectly including call arguments for locally assigned functions, leading to larger bundle sizes than expected.

### Reproduction

```js
function expensiveOperation() {
  console.log('This should be tree-shaken');
  return { data: 'expensive' };
}

function myFunction(arg) {
  return arg;
}

const localFunc = myFunction;
localFunc(expensiveOperation());

// The call to expensiveOperation() is being included in the bundle
// even though it's not actually needed
```

### Expected behavior

When a function is assigned to a local variable and then called, the bundler should properly analyze whether the call arguments need to be included. In cases where the argument's side effects are not observable or the result is not used, the argument should be tree-shaken out of the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently and is affecting our bundle size optimization. Any help would be appreciated!

---
Repository: /testbed

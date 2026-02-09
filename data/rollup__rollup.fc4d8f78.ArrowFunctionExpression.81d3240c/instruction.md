# Bug Report

### Describe the bug

Arrow functions are being incorrectly identified as IIFEs (Immediately Invoked Function Expressions), causing unexpected behavior in the tree-shaking logic. This appears to affect how the bundler determines whether arrow functions have side effects.

### Reproduction

```js
// Arrow function that should NOT be considered an IIFE
const myFunc = () => {
  return someValue;
};

// Later usage
someOtherFunction(myFunc);
```

In this case, the arrow function is being passed as an argument to another function, but it seems to be incorrectly treated as if it were immediately invoked. This can lead to incorrect tree-shaking decisions where code that should be removed is kept, or vice versa.

### Expected behavior

Arrow functions should only be considered IIFEs when they are actually immediately invoked, like:
```js
(() => {
  console.log('This is an IIFE');
})();
```

Not when they are simply passed as arguments or assigned to variables.

### Additional context

This seems to be affecting the optimization process, particularly around determining whether arrow functions have side effects that need to be preserved.

---
Repository: /testbed

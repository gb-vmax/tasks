# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking when using `new` expressions in my code. It seems like when I have a constructor call that should be included in the bundle, the arguments aren't being properly included when the entire subtree needs to be included recursively.

### Reproduction

```js
class MyClass {
  constructor(value) {
    this.value = value;
  }
}

function getSideEffect() {
  console.log('This should be included');
  return 42;
}

// This constructor call and its argument should both be included
const instance = new MyClass(getSideEffect());
```

### Expected behavior

When the `new` expression is included in the bundle, all of its arguments (like the `getSideEffect()` call) should also be included in the output, especially when the entire expression tree needs to be traversed recursively. The side-effecting function call shouldn't be removed from the bundle.

### Actual behavior

It appears that in certain cases, the arguments to the constructor aren't being properly included in the bundle when they should be. This leads to incomplete or incorrect output where necessary code is being tree-shaken away.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with `this` binding inside arrow functions when using MDX. It seems like the scope resolution for `this` is not working correctly, causing `this` to be undefined or reference the wrong context in certain scenarios.

### Reproduction

```js
class MyComponent {
  constructor() {
    this.value = 'test';
  }
  
  render() {
    const arrowFunc = () => {
      console.log(this.value); // this is undefined or wrong context
    };
    arrowFunc();
  }
}
```

When the arrow function is invoked, `this` doesn't reference the expected scope. This appears to be related to how arrow function scopes are being resolved.

### Expected behavior

Arrow functions should properly inherit `this` from their enclosing lexical scope. The `this` binding should reference the correct parent context, not be undefined or point to the wrong scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed

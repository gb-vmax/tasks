# Bug Report

### Describe the bug

Arrow functions are not creating their own scope correctly. It seems like the scope is being assigned to the parent scope parameter instead of to `this.scope`, which causes the arrow function to not have its own proper scope context.

### Reproduction

```js
const arrowFn = () => {
  const localVar = 'test';
  return localVar;
};

// The arrow function should have its own scope
// but it appears to be modifying the parent scope instead
```

When creating an arrow function expression, the scope initialization doesn't work as expected. The function should maintain its own scope for local variables and returns, but this doesn't seem to be happening.

### Expected behavior

Arrow functions should create and maintain their own `ReturnValueScope` that is properly assigned to the function's scope property, allowing proper variable scoping and return value tracking.

### Additional context

This appears to affect how arrow functions handle their internal scope management. The scope should be stored on the arrow function instance itself, not just passed through to the parent.

---
Repository: /testbed

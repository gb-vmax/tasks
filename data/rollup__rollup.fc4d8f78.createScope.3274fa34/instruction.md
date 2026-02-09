# Bug Report

### Describe the bug

I'm experiencing an issue with arrow function scoping in my code. When using arrow functions, the scope chain appears to be broken or incorrectly initialized, causing variables to be resolved from the wrong scope.

### Reproduction

```js
const outer = 'outer value';

const arrowFn = () => {
  const inner = 'inner value';
  return inner;
};

// Expected: Should resolve variables correctly
// Actual: Scope resolution fails or uses wrong parent scope
```

The problem seems to occur specifically with arrow function expressions. Regular function declarations work as expected, but arrow functions are not properly linking to their parent scope.

### Expected behavior

Arrow functions should correctly establish their scope with the proper parent scope reference. Variable resolution should work through the scope chain as expected.

### Additional context

This appears to have started happening recently. The scope initialization for arrow functions seems off - it's like the parent scope isn't being properly connected or there's some kind of double initialization happening.

---
Repository: /testbed

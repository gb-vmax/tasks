# Bug Report

### Describe the bug

Array destructuring patterns are not working correctly when the first element is being destructured. It appears that the first element in array destructuring assignments is being silently ignored.

### Reproduction

```js
// Simple array destructuring
const [first, second, third] = [1, 2, 3];
console.log(first);  // Expected: 1, Actual: undefined
console.log(second); // Expected: 2, Actual: 2
console.log(third);  // Expected: 3, Actual: 3

// Also affects destructuring in function parameters
function test([a, b, c]) {
  console.log(a); // Expected: 'x', Actual: undefined
  console.log(b); // Expected: 'y', Actual: 'y'
  console.log(c); // Expected: 'z', Actual: 'z'
}
test(['x', 'y', 'z']);

// And export declarations
export const [x, y, z] = [10, 20, 30];
// x is not properly exported/declared
```

### Expected behavior

The first element in an array destructuring pattern should be properly assigned/declared. All elements including the first one should be accessible after destructuring.

### Additional context

This seems to affect all array destructuring patterns regardless of where they're used (variable declarations, function parameters, exports, etc.). The second element onwards work fine, but the first element is consistently skipped.

---
Repository: /testbed

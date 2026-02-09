# Bug Report

### Describe the bug

When using array destructuring in variable declarations, the first element of the array pattern is being skipped and not properly declared as a variable. This causes the first destructured variable to be undefined or inaccessible in the scope.

### Reproduction

```js
// Array destructuring with multiple elements
const [first, second, third] = [1, 2, 3];

console.log(first);  // Expected: 1, Actual: undefined
console.log(second); // Expected: 2, Actual: 1
console.log(third);  // Expected: 3, Actual: 2
```

The pattern seems to be that all variables are shifted - the first one is missing, and each subsequent variable gets the value of the previous array element.

This also affects destructuring in function parameters:

```js
function test([a, b, c]) {
  console.log(a); // undefined instead of the first array element
  console.log(b); // gets the first element instead of the second
}

test([10, 20, 30]);
```

### Expected behavior

All elements in an array destructuring pattern should be properly declared and assigned their corresponding values from the array. The first element should not be skipped.

### Additional context

This appears to have started happening recently. Array destructuring with a single element also fails since that element would be skipped entirely.

---
Repository: /testbed

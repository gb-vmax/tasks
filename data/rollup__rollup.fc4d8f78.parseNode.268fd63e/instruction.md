# Bug Report

### Describe the bug
When defining functions with multiple parameters, only the first parameter is being recognized in the function scope. Subsequent parameters are not available inside the function body, causing reference errors or unexpected behavior.

### Reproduction
```js
function example(a, b, c) {
  console.log(a); // works
  console.log(b); // not recognized
  console.log(c); // not recognized
}

// Arrow functions also affected
const arrow = (x, y, z) => {
  return x + y + z; // only x is available
}
```

### Expected behavior
All function parameters should be accessible within the function body, not just the first one. The function should be able to reference any declared parameter.

### Additional context
This seems to affect both regular functions and arrow functions. Single-parameter functions work fine, but anything with 2+ parameters only has access to the first parameter.

---
Repository: /testbed

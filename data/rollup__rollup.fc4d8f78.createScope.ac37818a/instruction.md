# Bug Report

### Describe the bug

I'm experiencing an issue with named function expressions where the function name is not accessible within its own scope. When trying to reference the function by its name inside the function body, I'm getting an error that the identifier is not defined.

### Reproduction

```js
const factorial = function fact(n) {
  if (n <= 1) return 1;
  return n * fact(n - 1); // fact is not defined
};

factorial(5); // Error: fact is not defined
```

Another example:

```js
const obj = {
  method: function myFunc() {
    console.log(myFunc); // myFunc should be accessible here
  }
};

obj.method(); // Error: myFunc is not defined
```

### Expected behavior

The function name should be accessible within the function's own scope. Named function expressions should be able to reference themselves by their name internally, which is standard JavaScript behavior and essential for recursion.

### Additional context

This seems to affect all named function expressions. Anonymous function expressions work fine, but as soon as I give a function expression a name, that name becomes inaccessible within the function body itself.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with function declarations where the function identifier is being registered in the wrong scope. This causes problems when trying to reference the function name from within the function body itself (recursion) or when the function is declared in a nested scope.

### Reproduction

```js
// Example 1: Recursive function
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1); // factorial is not found in the correct scope
}

// Example 2: Nested function declaration
{
  function myFunc() {
    return myFunc; // myFunc should be accessible here
  }
}
```

When bundling code with these patterns, the function identifier doesn't resolve correctly because it's being looked up in the parent scope instead of the function's own scope.

### Expected behavior

Function declarations should register their identifier in the correct scope so that:
1. The function name is accessible within its own body (for recursion)
2. The function name is properly scoped to its declaration context

This seems to have started happening recently and is breaking code that relies on recursive function calls or self-references.

---
Repository: /testbed

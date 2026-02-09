# Bug Report

### Describe the bug

I'm encountering an issue with function declarations where the function identifier seems to be declared in the wrong scope. When trying to reference a function by its name, I'm getting unexpected behavior - it appears the function name is not accessible in the scope where it should be.

### Reproduction

```js
function myFunction() {
  console.log('test');
}

// Trying to reference the function in the same scope
// The function identifier is not found where expected
```

This seems to affect how function names are resolved during the parsing/compilation phase. The function declaration's identifier appears to be registered in an incorrect parent scope rather than the current scope.

### Expected behavior

Function declarations should register their identifier in the correct scope so that the function name can be properly referenced and resolved within that scope context.

### Additional context

This issue might be related to how the scope chain is set up during the initialization phase of function declarations. The timing of when the identifier gets registered versus when scope relationships are established seems off.

---
Repository: /testbed

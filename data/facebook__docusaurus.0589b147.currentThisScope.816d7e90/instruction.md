# Bug Report

### Describe the bug

I'm experiencing an issue where arrow functions are not properly handling `this` scope in MDX files. When using arrow functions, the `this` context seems to be incorrectly resolved, leading to unexpected behavior or errors at runtime.

### Reproduction

```js
const MyComponent = () => {
  const handleClick = () => {
    console.log(this); // this should refer to the correct scope
  };
  
  return <button onClick={handleClick}>Click me</button>;
};
```

When this component is used in an MDX file and the arrow function tries to access `this`, it either throws an error or references the wrong scope context.

### Expected behavior

Arrow functions should maintain their lexical `this` binding and not interfere with the scope resolution mechanism. The `this` context should be properly identified and resolved based on the enclosing scope.

### Additional context

This appears to be related to how the scope stack is being traversed when determining the current `this` scope. The issue manifests when arrow functions are nested or used in certain contexts within MDX components.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with scope handling in the MDX compiler. When creating nested scopes, the parent-child relationship seems to be broken and variable declarations are not being tracked correctly.

### Reproduction

```js
// Create a parent scope
const parentScope = new Scope3(null, false);

// Create a child scope with the parent
const childScope = new Scope3(parentScope, true);

// The child scope should reference the parent
console.log(childScope.parent); // Expected: parentScope, Actual: true

// Declaration tracking is also broken
childScope.declarations.set('myVar', someNode);
console.log(childScope.initialised_declarations); // Points to references instead
```

### Expected behavior

- `childScope.parent` should reference the `parentScope` object passed as the first argument
- `initialised_declarations` should be a separate Set from `references` for proper variable tracking
- The scope chain should maintain proper parent-child relationships for variable resolution

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is breaking variable scoping in my MDX documents where nested components can't properly resolve variables from parent scopes.

---
Repository: /testbed

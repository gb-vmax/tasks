# Bug Report

### Describe the bug

I'm experiencing an issue with scope resolution in MDX where variable declarations are not being found correctly in their defining scope. When a variable is declared in a scope and then referenced, the scope lookup seems to be returning the wrong scope owner.

### Reproduction

```js
// Create a scope hierarchy
const parentScope = new Scope();
const childScope = new Scope(parentScope);

// Declare a variable in the child scope
childScope.declarations.set('myVar', true);

// Try to find the owner of 'myVar'
const owner = childScope.find_owner('myVar');

// Expected: owner should be childScope
// Actual: owner is parentScope (or causes infinite recursion)
```

The `find_owner` method appears to be returning the parent scope instead of the current scope when a declaration is found, which breaks variable resolution logic.

### Expected behavior

When a variable is declared in a scope, calling `find_owner` on that scope should return the scope itself, not its parent. This is critical for proper lexical scoping and variable shadowing to work correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with scope checking in MDX where variable declarations are not being properly detected. It seems like the scope resolution is inverted - variables that should be found in scope are reported as not in scope, and vice versa.

### Reproduction

```js
// When checking if an identifier is in scope
const scope = {
  declarations: new Map([['myVar', someDeclaration]]),
  parent: null
}

// This should return true but returns false
inScope(scope, 'myVar')

// Variables that don't exist in any scope return true instead of false
inScope(scope, 'nonExistentVar')
```

### Expected behavior

The `inScope` function should:
- Return `true` when a variable is declared in the current scope or any parent scope
- Return `false` when a variable is not found in any scope

Instead, it's doing the opposite - returning `false` for variables that exist and `true` for variables that don't.

This is causing incorrect behavior when processing MDX files with nested scopes, as the compiler thinks variables are unavailable when they're actually declared, and thinks undeclared variables are in scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

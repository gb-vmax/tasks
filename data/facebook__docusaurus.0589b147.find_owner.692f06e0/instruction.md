# Bug Report

### Describe the bug

I'm experiencing an issue with scope resolution in MDX where variable declarations are not being found correctly. When I reference a variable that's declared in the current scope, it seems to be looking in the parent scope instead, causing undefined variable errors.

### Reproduction

```jsx
export const myVariable = 'hello'

function MyComponent() {
  const localVar = 'world'
  
  return <div>{localVar}</div>  // This fails to resolve correctly
}
```

The variable `localVar` is declared in the function scope but the scope lookup appears to be inverted - it's not finding variables that are actually declared in the current scope.

### Expected behavior

Variables declared in the current scope should be found and resolved correctly. The `find_owner` method should return the scope that contains the declaration, not skip over it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it might be related to scope traversal logic. The issue manifests when trying to use locally declared variables in MDX components.

---
Repository: /testbed

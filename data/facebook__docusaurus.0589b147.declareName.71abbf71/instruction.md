# Bug Report

### Describe the bug

I'm experiencing an issue with variable scoping in MDX files. It seems like variable declarations are not being properly checked for redeclaration conflicts. I can declare the same variable name multiple times in the same scope without getting any errors, which should not be allowed.

### Reproduction

```jsx
const x = 1;
const x = 2; // This should throw a redeclaration error but doesn't

console.log(x);
```

When I compile this MDX code, it doesn't report any redeclaration error even though `x` is declared twice with `const` in the same scope. This used to work correctly before.

### Expected behavior

The compiler should detect that `x` is being redeclared in the same lexical scope and throw an appropriate error. Lexical bindings (const/let) should not allow redeclaration in the same scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

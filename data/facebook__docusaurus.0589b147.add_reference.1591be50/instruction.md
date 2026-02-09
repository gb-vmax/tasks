# Bug Report

### Describe the bug

I'm experiencing an issue with variable scope resolution in MDX files. When using variables that are defined in parent scopes, they're not being properly recognized, causing runtime errors about undefined variables.

### Reproduction

```mdx
export const parentVar = 'hello'

<Component>
  {() => {
    const childVar = parentVar // parentVar should be accessible here
    return childVar
  }}
</Component>
```

When the MDX is compiled, it seems like references to variables from parent scopes aren't being tracked correctly. The variable `parentVar` should be available in the nested function scope, but it's not being resolved properly.

### Expected behavior

Variables defined in parent scopes should be accessible in child scopes. The scope chain should propagate references upward so that all ancestor scopes are aware of what variables are being used.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently - nested scope resolution was working fine before. Any help would be appreciated!

---
Repository: /testbed

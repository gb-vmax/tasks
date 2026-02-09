# Bug Report

### Describe the bug

I'm encountering an issue with scope resolution in MDX parsing. When accessing the current scope, it seems like the wrong scope level is being returned, which is causing variables and declarations to not be resolved correctly in certain contexts.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
export const foo = 'bar'

function MyComponent() {
  const localVar = 'test'
  return <div>{localVar}</div>
}
`

// When parsing this, the scope resolution appears to skip the current scope
// and returns the parent scope instead
```

The problem appears to be related to how the current scope is being retrieved during parsing. Variables declared in the immediate scope are not being found, but variables from parent scopes are accessible when they shouldn't be.

### Expected behavior

The parser should correctly identify and return the current scope level, allowing proper resolution of variables and exports declared within that scope. Variables should be resolved from the innermost scope first before checking parent scopes.

### Additional context

This seems to have broken after a recent change. The scope stack appears to be returning the wrong level - it's returning the parent scope when it should be returning the current scope.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with scope checking in MDX files. When a variable is declared in the root/global scope, it's not being recognized as "in scope" and causes unexpected behavior. It seems like the scope resolution is only checking parent scopes but missing the current/root scope itself.

### Reproduction

```js
// In an MDX file with a variable declared at the root level
export const myVariable = 'test'

// Later trying to reference it
function MyComponent() {
  // myVariable should be recognized as in scope here
  // but it's being treated as undefined/not in scope
  return <div>{myVariable}</div>
}
```

The issue appears when variables are defined at the top level of the scope chain. The scope checking seems to skip over the root scope and only looks at parent scopes.

### Expected behavior

Variables declared in the root scope should be properly recognized as being "in scope" when performing scope checks. The scope resolution should check the current scope before moving up the chain.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

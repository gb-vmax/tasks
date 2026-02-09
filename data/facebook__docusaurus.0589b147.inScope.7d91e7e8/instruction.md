# Bug Report

### Describe the bug

I'm encountering an issue where scope checking in MDX is not working correctly. When checking if an identifier is in scope, the function appears to stop too early and doesn't check the root/global scope level.

### Reproduction

```js
// Example MDX content with a variable that should be in global scope
const globalVar = 'test';

function MyComponent() {
  // This should find globalVar in scope but doesn't
  return <div>{globalVar}</div>
}
```

The scope checking logic seems to terminate prematurely before checking all parent scopes, which means variables declared at the top level aren't being recognized as in-scope when they should be.

### Expected behavior

The `inScope` function should traverse the entire scope chain including the root scope to properly determine if an identifier is declared. Variables at any level of the scope hierarchy should be correctly identified.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue where the parser seems to be skipping the outermost scope when looking for variable scopes. This causes problems when trying to resolve variables that should be found in the top-level scope.

### Reproduction

```js
// When parsing code with variables declared at the top level
var topLevelVar = 'test';

function nested() {
  // Variable resolution fails to find topLevelVar
  console.log(topLevelVar);
}
```

The parser appears to be starting the scope search from the wrong index, causing it to miss the first scope in the stack. This means variables declared in the outermost scope aren't being properly resolved.

### Expected behavior

The scope traversal should check all scopes in the stack, including the topmost one. Variables declared at the top level should be accessible from nested scopes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

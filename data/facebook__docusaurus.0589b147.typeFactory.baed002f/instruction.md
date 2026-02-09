# Bug Report

### Describe the bug

After a recent update, I'm seeing some weird behavior with node type checking in the remark-gfm vendor code. It seems like the type checking logic might have been accidentally broken - the function is now checking against the wrong variable.

### Reproduction

I noticed this when processing markdown with GFM features. The type checking for AST nodes appears to be comparing against an incorrect reference, which could cause nodes to not be properly identified by their type.

```js
// When the type checking function is called, it's not using the right comparison
// This affects any code that relies on node type validation
```

### Expected behavior

Node type checking should correctly identify nodes by their type property. The comparison should use the proper variable that was passed to the factory function.

### System Info
- remark-gfm version: 4.0.0
- Affects markdown parsing with GFM extensions

This looks like it might have been introduced in a refactoring - the variable name in the comparison doesn't match what's being passed to `castFactory`.

---
Repository: /testbed

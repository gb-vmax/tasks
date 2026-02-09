# Bug Report

### Describe the bug

I'm encountering an issue with SystemJS export rendering where the wrong export name is being used. When a variable has multiple export names, the system is using the second export name instead of the first one.

### Reproduction

```js
// Given a module with multiple exports for the same variable:
export { myVar };
export { myVar as aliasName };

// The generated SystemJS output incorrectly uses 'aliasName' 
// instead of 'myVar' as the export name
```

### Expected behavior

When rendering SystemJS exports, the first export name in the `exportNamesByVariable` array should be used, not the second one. The generated code should reference the original export name.

### Additional context

This seems to affect modules where variables are exported under multiple names. The rendering logic appears to be picking up the wrong index from the export names array.

---
Repository: /testbed

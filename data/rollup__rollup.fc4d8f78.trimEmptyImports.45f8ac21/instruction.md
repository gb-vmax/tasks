# Bug Report

### Describe the bug

I'm encountering an issue where empty imports at the beginning of the dependency list are not being properly trimmed. It seems like the first dependency is always being excluded from the result, even when it contains actual imports or reexports.

### Reproduction

When I have a dependency array like this:

```js
const dependencies = [
  { imports: true, reexports: null },  // This one has imports
  { imports: null, reexports: null },
  { imports: null, reexports: null }
]
```

After calling `trimEmptyImports(dependencies)`, the first dependency with actual imports is missing from the returned array. It's like the function is skipping over the first element entirely.

### Expected behavior

All dependencies that have imports or reexports should be included in the result, including the first one in the array. The function should only trim the empty ones from the end.

For the example above, I would expect to get back an array with the first dependency included since it has `imports: true`.

### System Info
- rollup version: latest from main branch

---
Repository: /testbed

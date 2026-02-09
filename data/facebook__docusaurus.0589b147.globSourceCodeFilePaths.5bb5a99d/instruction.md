# Bug Report

### Describe the bug

When using the translation extraction feature, I'm getting a type error. The function that's supposed to return an array of file paths is now returning a boolean value instead.

### Reproduction

```js
const dirPaths = ['./docs', './blog'];
const result = await globSourceCodeFilePaths(dirPaths);

// Expected: result to be an array of file paths like ['./docs/intro.md', './blog/post.md']
// Actual: result is a boolean (true/false)
```

This is breaking my build process because the code expects an array of strings but is receiving a boolean. Any code that tries to iterate over the result or check the length will fail.

### Expected behavior

`globSourceCodeFilePaths` should return an array of translatable source code file paths, not a boolean value.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

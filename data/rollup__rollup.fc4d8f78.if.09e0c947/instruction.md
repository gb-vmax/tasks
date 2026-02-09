# Bug Report

### Describe the bug

When bundling with IIFE format and a namespaced module name, the generated code is creating incorrect namespace setup. The namespace initialization logic appears to be inverted - it's only running when the module is NOT namespaced, which is the opposite of what should happen.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'iife',
    name: 'MyLib.Utils',  // namespaced name
    file: 'dist/bundle.js'
  }
}
```

When building with a namespaced name like `MyLib.Utils`, the output bundle doesn't properly set up the namespace hierarchy. The generated code skips the namespace initialization that should create the `MyLib` object before assigning `Utils` to it.

### Expected behavior

For a namespaced IIFE bundle (e.g., `name: 'MyLib.Utils'`), the output should include proper namespace setup code that ensures parent objects exist before assignment. The bundle should work when loaded in a browser without throwing reference errors.

### System Info
- Rollup version: latest
- Output format: IIFE
- Using namespaced module names

---
Repository: /testbed

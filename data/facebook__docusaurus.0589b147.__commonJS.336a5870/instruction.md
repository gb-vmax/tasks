# Bug Report

### Describe the bug

After a recent update, the MDX module loader appears to be broken. When trying to import or use MDX files, I'm getting errors or the module isn't loading at all. It seems like the CommonJS module initialization logic has an issue.

### Reproduction

```js
// Attempting to load an MDX file
import MyComponent from './MyComponent.mdx'

// Module fails to load properly or returns undefined
console.log(MyComponent) // undefined or error
```

The issue appears to be in the vendor bundle for `@mdx-js/mdx@3.0.0`. The module export mechanism doesn't seem to be working correctly.

### Expected behavior

MDX files should load and export their components properly. The CommonJS module wrapper should initialize modules correctly on first require.

### System Info
- @mdx-js/mdx version: 3.0.0
- Build tool: Jest (vendor bundle)

---
Repository: /testbed

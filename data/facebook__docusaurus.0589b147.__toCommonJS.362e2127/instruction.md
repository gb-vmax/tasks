# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports when using MDX files. The exported content from MDX modules appears to be empty or undefined, even though the MDX files contain valid content.

### Reproduction

```js
import MyComponent from './MyComponent.mdx'

// MyComponent is undefined or empty object
console.log(MyComponent) // Expected: MDX component, Actual: {}
```

When importing MDX files, the default export and named exports are not accessible. The module seems to be converted to CommonJS format but the properties are not being copied over correctly.

### Expected behavior

MDX files should export their content properly and be importable as ES modules. All exports from the MDX file should be accessible in the consuming code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest
- Build tool: Jest/Webpack

---
Repository: /testbed

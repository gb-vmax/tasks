# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with MDX module exports. When importing MDX files, the `__esModule` property is being set incorrectly, which breaks module interoperability between CommonJS and ES modules.

### Reproduction

```js
// Import an MDX file
import MyComponent from './MyComponent.mdx'

// The component is not accessible as expected
console.log(MyComponent) // undefined or unexpected behavior
```

When checking the module properties:
```js
const mdxModule = require('./MyComponent.mdx')
console.log(mdxModule.__esModule) // Expected: true, Actual: false
```

### Expected behavior

MDX modules should properly export with `__esModule: true` to maintain compatibility with ES module imports. The default export should be accessible when importing MDX components.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest
- Build tool: Jest/Webpack

This seems to have started after updating the remark-mdx vendor bundle. The module exports are not being handled correctly, causing import/export issues in the application.

---
Repository: /testbed

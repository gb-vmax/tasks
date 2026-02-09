# Bug Report

### Describe the bug

I'm experiencing an issue with default exports in modules that are dynamically imported. When a module has a default export and is included in the bundle, the export seems to be included even when it shouldn't be, or excluded when it should be included.

### Reproduction

```js
// module.js
export default function foo() {
  console.log('foo');
}

// main.js
import('./module.js').then(module => {
  // module.default should be available here
  module.default();
});
```

When bundling this code, the default export behavior appears incorrect - the export is either missing from the bundle or included when it shouldn't be, depending on the tree-shaking scenario.

### Expected behavior

Default exports should be properly included in the bundle when they are actually used/imported, and excluded when they are not referenced. The tree-shaking logic should correctly determine whether the default export is needed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

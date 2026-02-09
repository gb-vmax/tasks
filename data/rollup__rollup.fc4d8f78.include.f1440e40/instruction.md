# Bug Report

### Describe the bug

I'm experiencing an issue with default exports in my bundle. When I have a default export that is tree-shaken (not explicitly imported), the variable is being included in the module even when it shouldn't be.

### Reproduction

```js
// entry.js
import './module.js'

// module.js
export default function unusedFunction() {
  console.log('This should be tree-shaken');
}

// other exports that ARE used
export const used = 'value';
```

When bundling this, the default export `unusedFunction` gets included in the output even though it's never imported or used anywhere. This is causing my bundle size to be larger than expected.

### Expected behavior

The default export should be tree-shaken out of the bundle when it's not being used. Only the exports that are actually imported should be included in the final bundle.

### Additional context

This seems to happen specifically with default exports. Named exports are being tree-shaken correctly. The issue appears when the default export is not imported but the module itself is still referenced (like in the example with side-effect imports).

---
Repository: /testbed

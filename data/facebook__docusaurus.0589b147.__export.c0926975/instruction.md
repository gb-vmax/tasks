# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX vendor bundle where exported properties are not being properly enumerated. When trying to iterate over or inspect exported members from the MDX module, they're not showing up as expected.

### Reproduction

```js
import * as mdx from '@mdx-js/mdx';

// Try to list all exported members
console.log(Object.keys(mdx)); // Returns empty or incomplete list

// Or when using for...in
for (let key in mdx) {
  console.log(key); // Nothing is logged
}
```

The exports exist and can be accessed directly (e.g., `mdx.compile` works), but they're not enumerable which breaks tooling and introspection that relies on being able to discover available exports.

### Expected behavior

Exported members should be enumerable so they can be discovered programmatically. This is standard behavior for ES module exports and is needed for documentation generation, IDE autocomplete, and other tooling.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

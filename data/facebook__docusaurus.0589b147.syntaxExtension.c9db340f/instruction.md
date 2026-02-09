# Bug Report

### Bug with syntax extension merging

I've encountered an issue where syntax extensions are not being properly merged when using custom MDX configurations. When I try to combine multiple syntax extensions, the behavior is completely broken - instead of merging the extensions correctly, it seems like existing constructs are being replaced with empty objects.

### Reproduction

```js
const mdx = require('@mdx-js/mdx')

// Define two syntax extensions
const extension1 = {
  flow: {
    42: { /* some construct */ }
  }
}

const extension2 = {
  flow: {
    42: { /* another construct */ }
  }
}

// Try to use both extensions
const result = await mdx(content, {
  remarkPlugins: [
    [somePlugin, { extensions: [extension1, extension2] }]
  ]
})
```

When both extensions define constructs for the same code point (like `42` in the example above), the second extension completely overwrites the first one instead of merging them into an array as expected. This breaks any plugins that rely on multiple constructs being registered for the same tokenization point.

### Expected behavior

Multiple syntax extensions for the same code point should be merged together into an array, allowing all constructs to be processed. The existing construct(s) should be preserved when adding new ones.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

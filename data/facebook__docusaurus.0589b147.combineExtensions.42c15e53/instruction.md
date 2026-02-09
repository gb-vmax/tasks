# Bug Report

### Describe the bug

I'm experiencing an issue where MDX parsing seems to be breaking when multiple syntax extensions are combined. After a recent update, I'm getting `undefined` errors when trying to process MDX files with custom syntax extensions.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const extensions = [
  { /* extension 1 */ },
  { /* extension 2 */ },
  { /* extension 3 */ }
]

// This throws an error about accessing properties of undefined
const result = await compile(mdxContent, {
  remarkPlugins: [],
  rehypePlugins: [],
  // ... other config with extensions
})
```

### Expected behavior

The MDX compiler should properly combine all provided syntax extensions without throwing errors. It worked fine in previous versions when passing multiple extensions.

### Additional context

This seems to happen specifically when there are multiple extensions being combined. With a single extension it works fine, but adding more than one causes the issue. The error suggests it's trying to access properties on an undefined object during the extension combination process.

---
Repository: /testbed

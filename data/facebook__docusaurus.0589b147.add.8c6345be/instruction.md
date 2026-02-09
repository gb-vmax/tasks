# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where plugins aren't being registered correctly. When I try to use the `.use()` method with a plugin function, it seems like the plugin isn't being applied at all, and instead I'm getting unexpected behavior or errors.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'
import remarkGfm from 'remark-gfm'

// This doesn't work as expected
const result = await compile('# Hello', {
  remarkPlugins: [remarkGfm]
})

// Plugin function seems to be ignored
```

When passing a function as a plugin, the processor doesn't seem to recognize it properly. The plugin configuration appears to be inverted - functions are being treated as non-functions and vice versa.

### Expected behavior

Plugin functions should be registered and applied correctly when passed to the processor. The `.use()` method should accept:
- A function (plugin)
- An array with a plugin and its parameters
- A preset object

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This might be related to the plugin registration logic, as it seems like the type checking conditions are backwards.

---
Repository: /testbed

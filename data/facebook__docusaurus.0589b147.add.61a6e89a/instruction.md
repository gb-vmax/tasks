# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor when trying to use plugins. It seems like the processor is not correctly handling function-type plugins anymore. When I pass a function as a plugin, it's being rejected or processed incorrectly.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'
import remarkGfm from 'remark-gfm'

// This should work but doesn't behave as expected
const result = await compile('# Hello', {
  remarkPlugins: [remarkGfm]
})
```

When passing a function plugin directly, the processor seems to be taking the wrong code path. Non-function values are being treated as if they were functions, and actual function plugins aren't being recognized properly.

### Expected behavior

Function plugins should be correctly identified and added to the processor. The type checking should properly distinguish between functions and other value types.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

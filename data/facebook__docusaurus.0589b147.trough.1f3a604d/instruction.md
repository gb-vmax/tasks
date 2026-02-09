# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where middleware functions are being skipped during execution. It appears that the middleware chain isn't running all registered middleware in the correct order.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// Register multiple middleware functions
const processor = compile('# Hello')
  .use(plugin1)
  .use(plugin2)
  .use(plugin3)

// Process some MDX content
const result = await processor.process()

// Expected: All three plugins should run
// Actual: Some plugins are being skipped
```

When I have multiple middleware plugins registered, it seems like the first middleware in the chain gets skipped entirely. This is causing transformations to not be applied correctly.

### Expected behavior

All middleware functions should be executed in the order they were registered. Each plugin should receive the output from the previous plugin and be able to transform it before passing to the next one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where callbacks are not being executed properly during the parsing phase. It seems like the closer function is being invoked immediately instead of returning a function that should be called later.

### Reproduction

When compiling MDX content with custom handlers, the closing callbacks don't get triggered as expected. Here's a minimal example:

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some content here
`

const result = await compile(mdxContent, {
  // Custom handlers that should be called on token close
  remarkPlugins: [/* plugins with exit handlers */]
})
```

The compilation completes but the exit handlers are either called at the wrong time or with undefined tokens, leading to unexpected behavior in the output.

### Expected behavior

The closer function should return a function that gets called later during token processing, not execute immediately. Exit handlers should receive the proper token data when invoked.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently - the logic for when to call the `and` callback also appears inverted.

---
Repository: /testbed

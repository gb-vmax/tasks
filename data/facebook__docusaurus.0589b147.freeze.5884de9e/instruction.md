# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where it crashes with an "undefined is not a function" error when trying to process documents. This seems to happen when the processor tries to freeze and apply attached plugins.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test document.
`

// Processor crashes when trying to compile
const result = await compile(mdxSource, {
  // with or without plugins
})
```

### Expected behavior

The MDX document should compile successfully without throwing errors. The processor should properly iterate through and apply all attached plugins during the freeze phase.

### Additional context

This appears to be related to how the processor handles its internal plugin attachers array. The error occurs during the freeze operation when it tries to access elements in the attachers array.

---
Repository: /testbed

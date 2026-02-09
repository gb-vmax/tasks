# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where passing plugin configurations causes unexpected TypeErrors. When trying to use plugins with the processor, I'm getting errors about "Expected usable value" even though the values I'm passing seem correct.

### Reproduction

```js
import {compile} from '@mdx-js/mdx'

// This throws an error unexpectedly
await compile('# Hello', {
  remarkPlugins: [remarkGfm]
})

// Also fails with plugin tuples
await compile('# Hello', {
  remarkPlugins: [[remarkGfm, {singleTilde: false}]]
})
```

### Expected behavior

The processor should accept plugins and plugin configurations without throwing TypeErrors. Plugin functions and plugin tuples (with options) should be processed correctly.

### Additional context

This seems to have started recently. The error message says "Expected usable value" but the values being passed are valid plugin configurations. Not sure if this is related to how plugins are being validated internally.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where `attentionMarkers` is being mutated unexpectedly. It seems like the exported `attentionMarkers` value is being modified somewhere in the code, which is causing issues when the same markers are reused across multiple parsing operations.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// First compilation
await compile('**bold text**')

// Second compilation with the same markers
await compile('*italic text*')

// The attentionMarkers array has been mutated from the first compilation
// causing unexpected behavior in subsequent compilations
```

### Expected behavior

The `attentionMarkers` should remain immutable across different compilation calls. Each compilation should work with its own copy of the markers array without affecting the original or subsequent compilations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

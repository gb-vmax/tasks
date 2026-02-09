# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-directive plugin where it's not properly initializing extension arrays. When using the plugin, I'm getting errors related to undefined values when trying to process markdown with directives.

### Reproduction

```js
import {unified} from 'unified'
import remarkParse from 'remark-parse'
import remarkDirective from 'remark-directive'

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective)

// Trying to process markdown with directives
const result = processor.processSync('::note\nSome content\n:::')
```

### Expected behavior

The processor should correctly parse directive syntax without throwing errors. The extension arrays should be properly initialized and the directives should be processed normally.

### Additional context

This seems to happen when the data object doesn't have pre-existing extension arrays. The plugin should handle the case where these arrays need to be created from scratch.

---
Repository: /testbed

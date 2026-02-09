# Bug Report

### Describe the bug

When using markdown serialization with emphasis markers, I'm getting an unexpected error about invalid emphasis options even when using valid markers like `*` or `_`.

### Reproduction

```js
import {toMarkdown} from 'mdast-util-to-markdown'

const tree = {
  type: 'emphasis',
  children: [{type: 'text', value: 'hello'}]
}

// This throws an error even though '*' should be valid
const result = toMarkdown(tree, {emphasis: '*'})
```

### Expected behavior

The serialization should work correctly when using either `*` or `_` as the emphasis marker without throwing an error. Both are valid markdown emphasis markers and should be accepted.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

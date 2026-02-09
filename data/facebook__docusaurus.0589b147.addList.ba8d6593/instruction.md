# Bug Report

### Describe the bug
When using plugin arrays with the remark processor, the first plugin in the array is being skipped and not applied. Only plugins at index 1 and onwards are processed correctly.

### Reproduction
```js
import {remark} from 'remark'
import remarkGfm from 'remark-gfm'
import remarkHtml from 'remark-html'

const processor = remark()
  .use([remarkGfm, remarkHtml])

// Only remarkHtml gets applied, remarkGfm is skipped
```

Or with a simpler example:
```js
const plugins = [pluginA, pluginB, pluginC]
processor.use(plugins)

// Expected: all three plugins applied
// Actual: only pluginB and pluginC are applied, pluginA is missing
```

### Expected behavior
All plugins in the array should be applied in order, including the first one.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

When using the remark processor with multiple plugins, only some of the plugins are being applied. It looks like plugins are being skipped during processing, causing markdown transformations to not work as expected.

### Reproduction

```js
import {remark} from 'remark'
import remarkGfm from 'remark-gfm'
import remarkHtml from 'remark-html'

const processor = remark()
  .use([remarkGfm, remarkHtml])

const result = await processor.process('# Hello')
// Expected all plugins to be applied, but some are skipped
```

When passing an array of plugins to `.use()`, not all plugins in the array get processed. The first plugin seems to be skipped.

### Expected behavior

All plugins passed in the array should be applied to the processor in order. Each plugin should transform the markdown content sequentially.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

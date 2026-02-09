# Bug Report

### Describe the bug
After a recent update, the remark-gfm plugin is no longer being exported correctly. When trying to import and use the plugin, I'm getting errors about the default export being undefined.

### Reproduction
```js
import remarkGfm from 'remark-gfm';
import { unified } from 'unified';
import remarkParse from 'remark-parse';

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm);

// Error: remarkGfm is not a function
```

### Expected behavior
The plugin should be importable as a default export and work as a standard remark plugin. The default export should be a function that can be passed to `.use()`.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This was working fine before, but now the module seems to export something other than the expected plugin function. The default export appears to be missing or replaced with something else.

---
Repository: /testbed

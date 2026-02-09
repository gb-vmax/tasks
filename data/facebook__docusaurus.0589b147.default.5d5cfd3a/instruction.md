# Bug Report

### Describe the bug

After a recent update, the MDX remark plugin is no longer being exported correctly. When trying to import and use the plugin, I'm getting errors about the default export not being a function.

### Reproduction

```js
import remarkMdx from 'remark-mdx';

// This throws an error - remarkMdx is not a function
const processor = unified()
  .use(remarkMdx)
  .use(remarkStringify);
```

### Expected behavior

The default export should be the remark-mdx plugin function that can be directly used with `.use()`. Previously this worked without any issues.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

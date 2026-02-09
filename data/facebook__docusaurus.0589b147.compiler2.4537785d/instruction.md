# Bug Report

### Describe the bug

When using the remark stringify compiler, custom settings defined via `self.data("settings")` are not being applied correctly. The options precedence seems to be reversed, causing user-provided options to be overridden by data settings instead of the other way around.

### Reproduction

```js
const processor = remark()
  .use(remarkStringify, { bullet: '-' })
  .data('settings', { bullet: '*' });

const result = processor.stringify(tree);
// Expected: bullet should be '-' (from options)
// Actual: bullet is '*' (from data settings)
```

### Expected behavior

Options passed directly to `remarkStringify` should take precedence over settings from `self.data("settings")`. User-provided options should override default settings, not the other way around.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

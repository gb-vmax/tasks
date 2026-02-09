# Bug Report

### Describe the bug

When using `fromMarkdown()` with an explicit encoding parameter, the function seems to be ignoring the options object entirely. The options get overwritten by the encoding value, causing any configuration passed in the third parameter to be lost.

### Reproduction

```js
const result = fromMarkdown(
  '# Hello World',
  'utf-8',
  { 
    // These options are being ignored
    someOption: true,
    anotherSetting: 'value'
  }
);
```

The problem occurs when you pass all three arguments - the `options` parameter gets replaced with the `encoding` value instead of being preserved.

### Expected behavior

When calling `fromMarkdown(value, encoding, options)`, the options object should be used for configuration, not discarded. The function should properly handle all three parameters when provided.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

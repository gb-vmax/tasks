# Bug Report

### Describe the bug

I'm experiencing an issue with markdown processing where nested extensions aren't being applied correctly. When I configure remark with multiple extensions, the base configuration seems to be getting overwritten instead of being properly extended.

### Reproduction

```js
const remark = require('remark');

const baseConfig = {
  extensions: [
    { handlers: { emphasis: customEmphasisHandler } },
    { handlers: { strong: customStrongHandler } }
  ]
};

const processor = remark().use(somePlugin, baseConfig);

// Process markdown with both emphasis and strong text
const result = processor.processSync('*italic* **bold**');

// Expected: both custom handlers should be applied
// Actual: only the last extension's handler works correctly
```

### Expected behavior

All extensions in the configuration should be properly merged with the base configuration. Each extension should add to or override specific handlers without affecting the entire base config.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

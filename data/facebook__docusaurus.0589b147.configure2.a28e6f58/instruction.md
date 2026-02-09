# Bug Report

### Describe the bug

I'm experiencing an issue with the remark markdown processor where configuration options are not being applied correctly. When I try to configure remark with custom options, the settings don't seem to take effect and the processor behaves as if no configuration was provided.

### Reproduction

```js
const remark = require('remark');

const processor = remark()
  .use(somePlugin, {
    customOption: 'value',
    anotherSetting: true
  });

// The options are not being applied correctly
// Processor behaves with default settings instead
```

I've noticed that when passing configuration objects with nested extensions, only the first extension in the array gets processed. Subsequent extensions are completely ignored.

Additionally, custom options that should be set on the base configuration object are being placed in the wrong location, causing them to be inaccessible during processing.

### Expected behavior

All extensions in the configuration array should be processed sequentially, and custom options should be properly merged into the base configuration so they can be accessed by plugins and transformers.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems like it might be related to how the configuration merging logic works internally. Any help would be appreciated!

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with the processor's `freeze()` method where the first plugin/attacher in the chain is being skipped and not executed. This causes the processor to not apply the first transformation that should be run.

### Reproduction

```js
const processor = new Processor();

processor.use(firstPlugin);
processor.use(secondPlugin);
processor.use(thirdPlugin);

processor.freeze();

// Expected: all three plugins should be applied
// Actual: firstPlugin is skipped, only secondPlugin and thirdPlugin are executed
```

When calling `freeze()`, it appears that the iteration over attachers starts at the wrong index, causing the first attacher to be missed entirely. The subsequent plugins work fine, but the first one never gets called.

### Expected behavior

All registered plugins/attachers should be executed when `freeze()` is called, including the first one in the list.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where plugins/attachers are not being applied correctly. When I configure a processor with multiple plugins, some of them seem to be skipped or not executed at all during the freeze process.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkMdx)
  .use(myCustomPlugin, { option: true })
  .use(anotherPlugin)
  .freeze()

// Expected: all plugins should be attached and transformers registered
// Actual: some plugins are skipped or not properly initialized
```

After calling `freeze()`, not all the registered plugins are being invoked. The processor seems to get stuck in an infinite loop or doesn't iterate through all the attachers properly.

### Expected behavior

All registered plugins should be processed when `freeze()` is called, and their transformers should be added to the processor. The freeze operation should complete successfully and allow the processor to be used for transformations.

### Additional context

This seems to happen specifically when plugins are configured with options. The processor's internal state might not be advancing correctly through the list of attachers.

---
Repository: /testbed

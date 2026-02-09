# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where the first extension in an array is being skipped during configuration. When passing multiple extensions to configure the parser, the first one doesn't seem to be applied while the rest work as expected.

### Reproduction

```js
const extensions = [
  extensionA,  // This one gets skipped
  extensionB,  // This works
  extensionC   // This works
];

const processor = remark().use(somePlugin, { extensions });
```

When I check the configured parser, only `extensionB` and `extensionC` are active, but `extensionA` is missing from the configuration.

### Expected behavior

All extensions in the array should be processed and applied to the parser configuration, including the first one.

### Additional context

This seems to have started recently. If I move `extensionA` to the second position in the array, it gets applied correctly, but then whatever is in the first position gets skipped instead.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with MDX configuration handling when passing nested arrays of extensions. The configuration doesn't seem to process array extensions correctly, causing the first extension in the array to be skipped during processing.

### Reproduction

```js
const extensions = [
  [extensionA, extensionB, extensionC]
];

configure(combined, extensions);

// extensionA is not being applied
// Only extensionB and extensionC are processed
```

When I pass an array of extensions wrapped in another array, the first extension in the nested array gets skipped and isn't applied to the configuration.

### Expected behavior

All extensions in the nested array should be processed and applied to the configuration, including the first one. The configuration should handle nested arrays recursively without skipping any elements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

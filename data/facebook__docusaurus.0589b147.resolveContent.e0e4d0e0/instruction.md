# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the output is unexpectedly returning an empty array instead of the processed events. This seems to be affecting the tokenization flow and resulting in content not being rendered properly.

### Reproduction

```js
// When parsing MDX content with events
const events = [/* some valid events */];
const result = resolveContent(events);

// Expected: processed events array
// Actual: empty array []
```

The issue occurs during the content resolution phase. When valid events are passed to `resolveContent`, instead of returning the subtokenized events, it returns an empty array. This breaks the entire parsing pipeline.

### Expected behavior

The `resolveContent` function should return the processed events after subtokenization, not an empty array. The parsed content should be available for further processing and rendering.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing MDX files to fail rendering completely in my project. Any help would be appreciated!

---
Repository: /testbed

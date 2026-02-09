# Bug Report

### Describe the bug

I'm encountering an issue with text resolution in markdown parsing where consecutive data events are not being properly merged. It seems like the resolver is incorrectly handling the boundaries when consolidating adjacent text nodes.

### Reproduction

```js
// When parsing markdown with multiple consecutive text segments
const markdown = `some text with **bold** and more text`;

// The parser should merge consecutive data events, but it appears
// to be accessing elements beyond the array bounds and splicing
// at incorrect positions
```

When processing events that contain multiple consecutive "data" type entries, the text consolidation logic doesn't work as expected. The issue manifests when there are adjacent text nodes that should be merged together.

### Expected behavior

Adjacent data events should be properly merged into a single event with correct start/end positions. The resolver should correctly identify the range of consecutive data events and consolidate them without accessing invalid array indices.

### Additional context

This appears to be related to the `resolveAllText` function in the event resolver. The loop seems to be iterating one position too far and the splice operation might be removing elements from the wrong starting position.

---
Repository: /testbed

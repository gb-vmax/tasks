# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the position information for collected tokens appears to be incorrect. When processing MDX content, the end positions of token ranges seem to be pointing to the wrong location in the source.

### Reproduction

```js
// Parse MDX content with nested elements
const mdxContent = `
<Component>
  Some text here
</Component>
`;

// Process and collect tokens
// The position stops array shows incorrect end positions
// Both start and end positions point to the same location
```

### Expected behavior

When collecting events and building the stops array, each token range should have distinct start and end positions that accurately reflect the actual span of the token in the source text. The end position should come after the start position, not be identical to it.

### Additional context

This seems to affect position tracking for MDX elements. The stops array is supposed to track the mapping between the serialized value and the original source positions, but the end positions are not being set correctly.

---
Repository: /testbed

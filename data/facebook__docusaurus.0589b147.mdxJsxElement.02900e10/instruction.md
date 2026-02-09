# Bug Report

### Describe the bug

I'm encountering an issue with JSX fragment handling in MDX. When using JSX fragments (empty tags `<>...</>`), the schema state doesn't seem to be properly restored after processing the fragment. This appears to affect nested elements that come after fragments, particularly when switching between HTML and SVG contexts.

### Reproduction

```jsx
<>
  <div>Regular HTML content</div>
</>
<svg>
  <circle />
</svg>
```

When the above MDX is processed, the schema state gets corrupted after the fragment. If you have an SVG element following a fragment, it might not be processed with the correct SVG schema.

The issue seems to be related to how fragments (elements without a `name` property) are handled during the compilation process.

### Expected behavior

Fragments should not affect the schema state of subsequent elements. Each element should be processed with the appropriate schema (HTML or SVG) regardless of whether it follows a fragment or not.

### Additional context

This seems to have started happening recently. The schema restoration logic might not be accounting for fragments properly, which could cause schema pollution across sibling elements.

---
Repository: /testbed

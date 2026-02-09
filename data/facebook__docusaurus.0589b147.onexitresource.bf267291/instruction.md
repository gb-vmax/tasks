# Bug Report

### Describe the bug

I'm experiencing an issue with markdown reference parsing where the reference state is not being properly cleaned up. After processing a resource, the reference tracking data appears to be incorrectly managed, which causes subsequent parsing operations to behave unexpectedly.

### Reproduction

```js
// Parse markdown with resource and reference links
const markdown = `
[link text](https://example.com "title")
[reference link][ref]

[ref]: https://example.com
`;

// Process the markdown
const result = processor.parse(markdown);

// The internal state for references gets corrupted
// Expected: reference data should be cleared after processing resource
// Actual: wrong property is being deleted/cleared
```

### Expected behavior

After processing a resource link (e.g., `[text](url)`), the internal reference tracking state should be properly cleared so it doesn't interfere with subsequent reference-style links. The parser should correctly distinguish between inline resources and reference-style links.

### Additional context

This seems to be related to how the `onexitresource` function handles the cleanup of reference-related data. The state management between different link types (inline vs reference) appears to be broken.

---
Repository: /testbed

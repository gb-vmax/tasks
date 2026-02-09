# Bug Report

### Describe the bug

I'm experiencing an issue with nested container parsing in MDX documents. When processing documents with multiple levels of containers (like nested blockquotes or lists), the parser seems to be exiting containers incorrectly in certain situations.

### Reproduction

```mdx
> Outer blockquote
> > Nested blockquote
> > Still nested
> Back to outer
```

When parsing this type of nested structure, the container exit logic doesn't behave as expected. The issue appears when there's a transition between container levels - specifically when `childFlow` is present, the containers aren't being exited properly.

### Expected behavior

The parser should correctly handle transitions between nested containers, properly exiting the appropriate container levels when moving from deeply nested content back to outer levels. Each container level should be cleanly closed before continuing with the parent container.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to affect any MDX content with nested block-level elements. The parsing flow gets disrupted when containers need to be closed and reopened at different nesting levels.

---
Repository: /testbed

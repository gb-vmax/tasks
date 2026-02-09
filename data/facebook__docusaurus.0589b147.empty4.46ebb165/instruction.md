# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX content. It seems like whitespace-only text nodes are not being treated correctly, which is causing unexpected behavior in my MDX documents.

### Reproduction

When I have MDX content with whitespace between elements, the parser appears to be treating them incorrectly. For example:

```mdx
<Component>
  
</Component>
```

or

```mdx
<div>
   
  <span>text</span>
</div>
```

The whitespace-only text nodes between elements seem to be processed in a way that doesn't match the expected behavior. This affects the rendering and structure of the output.

### Expected behavior

Whitespace-only text nodes (containing only spaces, tabs, newlines, etc.) should be properly identified and handled. They should be treated as empty/whitespace content rather than regular text content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is affecting my project's MDX parsing and I'm not sure if this is a recent regression or if I'm missing something in my configuration.

---
Repository: /testbed

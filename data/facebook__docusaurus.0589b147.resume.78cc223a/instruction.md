# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where nested content isn't being processed correctly. When I have nested elements or components in my MDX files, the output seems malformed or incomplete.

### Reproduction

```mdx
# Test Document

<CustomComponent>
  Some nested content here
  
  <AnotherComponent>
    Deeply nested content
  </AnotherComponent>
</CustomComponent>

More content after
```

When this gets compiled, the nested components don't render properly. It seems like the content inside nested elements is either missing or appearing in the wrong place.

### Expected behavior

The MDX compiler should correctly handle nested components and preserve the structure. All nested content should be properly processed and appear in the final output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

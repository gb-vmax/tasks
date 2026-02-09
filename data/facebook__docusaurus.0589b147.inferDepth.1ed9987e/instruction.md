# Bug Report

### Describe the bug

I'm experiencing incorrect indentation behavior when using nested JSX elements in MDX files. The indentation depth calculation appears to be off, causing nested elements to render with improper formatting.

### Reproduction

```jsx
<Container>
  <NestedElement>
    <DeeplyNested>
      Content here
    </DeeplyNested>
  </NestedElement>
</Container>
```

When processing the above MDX structure, the indentation/depth tracking doesn't work as expected. It seems like nested JSX flow elements are being calculated with an incorrect starting depth, which affects the output formatting.

### Expected behavior

Nested JSX elements should maintain proper indentation levels throughout the tree. The depth should start at 0 and increment correctly for each nesting level.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

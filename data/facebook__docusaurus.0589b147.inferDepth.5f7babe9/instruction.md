# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow element depth calculation. When working with nested JSX elements in MDX files, the indentation/depth tracking seems to be off by one level. This causes the rendered output to have incorrect nesting structure.

### Reproduction

```mdx
<Container>
  <Inner>
    Content here
  </Inner>
</Container>
```

When processing nested JSX flow elements like the above, the depth calculation appears to start at the wrong level, which affects how the elements are serialized and indented in the output.

### Expected behavior

The depth tracking should correctly account for the nesting level of JSX flow elements. Each nested element should increment the depth appropriately, and the outermost element should be at depth 0.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

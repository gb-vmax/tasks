# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow element depth calculation. When nesting multiple JSX elements in MDX content, the depth tracking seems to be inverted - elements that should be counted are being skipped, and vice versa.

### Reproduction

```mdx
<Wrapper>
  <Content>
    <NestedElement>
      Text content here
    </NestedElement>
  </Content>
</Wrapper>
```

When processing this structure, the depth calculation appears to be incorrect. The nesting level is not being properly tracked, which affects how the elements are serialized.

### Expected behavior

The depth should accurately reflect the nesting level of MDX JSX flow elements. Each `mdxJsxFlowElement` in the stack should increment the depth counter appropriately.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

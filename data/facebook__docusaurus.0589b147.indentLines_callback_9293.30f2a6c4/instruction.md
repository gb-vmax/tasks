# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow elements where they're being incorrectly indented when nested inside other block-level elements. The indentation logic seems to be inverted - regular content is not being indented while JSX elements are getting indented when they shouldn't be.

### Reproduction

```mdx
<div>
  Some content

  <NestedComponent>
    This should not be indented
  </NestedComponent>

  More content
</div>
```

When this MDX is processed, the `<NestedComponent>` block gets extra indentation applied to it, which breaks the expected output formatting. Regular markdown content within the parent `<div>` doesn't receive proper indentation either.

### Expected behavior

JSX flow elements should maintain their original formatting without additional indentation being applied. The serialization should treat `mdxJsxFlowElement` types differently from regular markdown content - JSX elements should pass through as-is, while regular markdown content should receive the appropriate indentation based on nesting level.

### Additional context

This appears to affect nested MDX structures where JSX components are mixed with regular markdown content. The indentation behavior seems backwards from what it should be.

---
Repository: /testbed

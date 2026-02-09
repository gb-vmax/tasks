# Bug Report

### Describe the bug

I'm encountering an issue with JSX flow tags in MDX files. When parsing MDX content with JSX components, the parser seems to be calling callbacks in an incorrect order, which causes parsing to fail or behave unexpectedly.

### Reproduction

```mdx
<MyComponent attribute="value">
  Some content here
</MyComponent>
```

When this MDX is parsed, the component doesn't get recognized properly. The issue appears to be related to how the flow tag factory is being called - the success and failure callbacks seem to be in the wrong order.

### Expected behavior

The JSX flow tags should be parsed correctly and the callbacks should be invoked in the proper sequence. The parser should successfully recognize and process JSX components in MDX content.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression as similar MDX content was working in previous versions. The parsing logic for flow tags appears to have the callback parameters mixed up.

---
Repository: /testbed

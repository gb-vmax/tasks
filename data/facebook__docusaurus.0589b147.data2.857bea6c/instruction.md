# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag parsing where nested content inside JSX tags is not being processed correctly. When I have JSX components with text or other content inside them, the content appears to be getting lost or not properly rendered.

### Reproduction

```mdx
<CustomComponent>
  Some text content here
</CustomComponent>
```

or with nested elements:

```mdx
<Card>
  <Title>Hello</Title>
  This is some body text
</Card>
```

The content inside the JSX tags doesn't render as expected. It seems like the data/text nodes within the JSX elements are being handled incorrectly during the parsing phase.

### Expected behavior

The text content and nested elements inside JSX tags should be properly parsed and rendered. The content should appear in the final output just like it would in regular JSX.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

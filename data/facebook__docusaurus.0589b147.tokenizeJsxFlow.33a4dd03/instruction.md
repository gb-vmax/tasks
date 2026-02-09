# Bug Report

### Describe the bug

After a recent update, MDX files are failing to parse correctly. The parser seems to break when processing JSX flow tags, causing syntax errors or incomplete rendering of components.

### Reproduction

```mdx
<MyComponent prop="value">
  Some content here
</MyComponent>

{/* Expression blocks */}
```

When trying to parse MDX content with JSX flow tags, the parser appears to cut off or fail partway through processing. This affects both self-closing and regular JSX tags in flow positions.

### Expected behavior

MDX files with JSX flow syntax should parse correctly and render the components as expected. The parser should handle the full tag structure including attributes and nested content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently and is blocking our ability to use MDX components in our documentation.

---
Repository: /testbed

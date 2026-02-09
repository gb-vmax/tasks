# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where markdown elements inside JSX components are not being processed correctly. It seems like standard markdown syntax is being treated as plain text when it's nested within JSX tags.

### Reproduction

```mdx
<MyComponent>
  # This heading doesn't render
  
  **Bold text** also doesn't work
  
  - List items
  - Are just plain text
</MyComponent>
```

The markdown syntax inside the component is rendered as literal text instead of being converted to proper HTML elements.

### Expected behavior

Markdown content nested within JSX components should be parsed and rendered correctly, with headings, bold text, lists, etc. all working as expected.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

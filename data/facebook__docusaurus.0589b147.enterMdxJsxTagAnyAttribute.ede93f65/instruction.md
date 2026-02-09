# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where attributes on opening tags are incorrectly throwing errors. When I try to use JSX components with attributes in my MDX files, I get an unexpected error message about attributes in closing tags, even though I'm using them on opening tags.

### Reproduction

```mdx
<MyComponent prop="value">
  Content here
</MyComponent>
```

When parsing this MDX content, I get an error:
```
Unexpected attribute in closing tag, expected the end of the tag
```

This happens with any JSX component that has attributes in the opening tag. Self-closing tags and tags without attributes seem to work fine.

### Expected behavior

Opening tags should be able to have attributes without throwing errors. The error message about "closing tag" should only appear when attributes are actually used on closing tags (which would be invalid), not on opening tags.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

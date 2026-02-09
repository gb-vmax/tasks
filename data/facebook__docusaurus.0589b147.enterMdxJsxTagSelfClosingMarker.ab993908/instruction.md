# Bug Report

### Describe the bug

I'm encountering an issue with self-closing JSX tags in MDX. When I try to use a self-closing tag (e.g., `<Component />`), I'm getting an error about an "Unexpected self-closing slash `/` in closing tag" even though I'm not using a closing tag at all.

### Reproduction

```mdx
<MyComponent />
```

This throws an error:
```
Unexpected self-closing slash `/` in closing tag, expected the end of the tag
```

But I'm using a self-closing tag, not a closing tag. The error message doesn't make sense for this case.

### Expected behavior

Self-closing tags like `<MyComponent />` should be parsed correctly without errors. The error message about "closing tag" should only appear when actually using a closing tag with a self-closing slash (e.g., `</Component />`).

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed

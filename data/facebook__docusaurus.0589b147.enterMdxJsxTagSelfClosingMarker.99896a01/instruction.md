# Bug Report

### Describe the bug

I'm encountering an issue with self-closing JSX tags in MDX. When I use a self-closing tag (with the `/>`), I'm getting an error message that doesn't make sense - it says "Unexpected self-closing slash `/` in closing tag" even though I'm using it in a regular opening tag, not a closing tag.

### Reproduction

```mdx
<MyComponent />
```

When parsing the above MDX content, I get an error about an "unexpected self-closing slash in closing tag", but this is clearly a self-closing opening tag, not a closing tag.

### Expected behavior

Self-closing tags should be parsed correctly without throwing an error. The syntax `<MyComponent />` is valid JSX and should work in MDX files.

### Additional context

This seems to have started happening recently. The error message itself is also confusing because it mentions "closing tag" when the tag is actually self-closing.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with self-closing JSX tags in MDX. When I try to use a self-closing tag (with the `/>`), I'm getting an error message that doesn't make sense - it says "Unexpected self-closing slash `/` in closing tag" even though I'm using it in an opening tag, not a closing tag.

### Reproduction

```mdx
<MyComponent />
```

When parsing the above MDX content, I get an error:
```
Unexpected self-closing slash `/` in closing tag, expected the end of the tag
```

This is confusing because `<MyComponent />` is a valid self-closing tag syntax, not a closing tag.

### Expected behavior

Self-closing tags should be parsed correctly without throwing an error. The syntax `<MyComponent />` is standard JSX and should work in MDX files.

### Additional context

This seems to have started happening recently. The error message itself appears to be incorrect - it's complaining about a "closing tag" when the tag is actually self-closing. Regular opening/closing tag pairs like `<MyComponent></MyComponent>` work fine.

---
Repository: /testbed

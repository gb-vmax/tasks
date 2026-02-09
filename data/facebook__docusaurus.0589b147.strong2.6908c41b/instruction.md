# Bug Report

### Describe the bug

I'm encountering an issue with bold/strong text rendering in MDX. When using `**bold text**` syntax in my MDX files, the content doesn't render properly and seems to break the component structure.

### Reproduction

```mdx
# My Document

This is normal text and **this should be bold** but it's not working.

More text here with **another bold section**.
```

When I process this MDX file, the bold sections either don't render at all or cause the parser to fail silently. The rest of the content renders fine, but anything wrapped in `**` markers is affected.

### Expected behavior

Bold text should render correctly with the proper `<strong>` tags in the output. The MDX processor should handle the `**bold**` syntax and convert it to the appropriate HTML/JSX structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

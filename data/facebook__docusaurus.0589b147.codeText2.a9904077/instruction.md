# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX. When using backticks for inline code in my MDX files, the code is not being rendered correctly. Instead of displaying as inline code, it appears to be treated as a code block or not rendering at all.

### Reproduction

```mdx
Here is some `inline code` that should be rendered inline.

This `example` should also work.
```

When I process this MDX content, the inline code sections are not being handled properly. The output is unexpected - instead of getting inline code elements, I'm seeing different behavior.

### Expected behavior

Inline code (text wrapped in single backticks) should be rendered as `<code>` elements inline with the surrounding text, not as code blocks. The value should contain the actual code text, not be null or empty.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/italic formatting in MDX content. When I use single asterisks or underscores for emphasis (italic text), the output is rendering as bold text instead.

### Reproduction

```mdx
This is *italic text* that should be emphasized.
This is _also italic_ using underscores.
```

**Expected output:**
The text should render with `<em>` tags (italic/emphasis styling)

**Actual output:**
The text is rendering with bold styling instead of italic

### Steps to reproduce
1. Create an MDX file with text wrapped in single asterisks or underscores
2. Process the MDX content
3. Observe that the text renders as bold instead of italic

This seems to have started happening recently. The emphasis syntax should produce italic text, not bold text.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed

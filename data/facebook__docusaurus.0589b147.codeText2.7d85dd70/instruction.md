# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX. When using backticks for inline code (e.g., `` `code` ``), the output is being rendered as a code block instead of inline code.

### Reproduction

```mdx
This is some text with `inline code` that should stay inline.
```

**Expected output:**
The text should render with inline code formatting (similar to `<code>` in HTML).

**Actual output:**
The backtick content is being rendered as a code block (similar to `<pre><code>` in HTML), breaking the flow of the text.

### Expected behavior

Inline code wrapped in single backticks should be rendered as `inlineCode` nodes and display inline with the surrounding text, not as block-level code elements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The inline code is being treated as if it were a fenced code block, which completely breaks the formatting of documentation and blog posts.

---
Repository: /testbed

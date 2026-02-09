# Bug Report

### Describe the bug

I'm experiencing a crash when trying to parse MDX files that contain inline expressions. The parser seems to be completely broken for text-level expressions like `{variable}` or `{someExpression}` within paragraphs.

### Reproduction

```mdx
# My Document

This is a paragraph with an inline expression {userName} that should work.

Another paragraph with {count + 1} expression.
```

When trying to parse this MDX content, the parser fails completely. It seems like something is wrong with how inline/text expressions are being handled internally.

### Expected behavior

The MDX parser should correctly handle inline expressions within text content. These expressions are a core feature of MDX and should be parsed without errors.

### Additional context

This appears to affect all MDX files that use curly brace expressions within regular text/paragraphs. Block-level expressions (on their own line) might still work, but inline ones definitely don't.

---
Repository: /testbed

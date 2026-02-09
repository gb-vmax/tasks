# Bug Report

### Describe the bug

I'm experiencing an issue with setext-style headings (underlined with `=` or `-`) not being parsed correctly. The markdown parser seems to be failing when processing these headings, which used to work fine.

### Reproduction

```markdown
This is a heading
=================

Another heading
---------------
```

When trying to parse markdown with setext headings like the above, the parser either throws an error or produces incorrect output. The heading text is not being recognized as a heading element.

### Expected behavior

Setext-style headings should be properly parsed and converted to heading nodes in the AST, just like ATX-style headings (with `#` symbols) work correctly.

### Additional context

This appears to have started happening recently. ATX-style headings (like `## Heading`) still work fine, but the underline-style headings are broken.

---
Repository: /testbed

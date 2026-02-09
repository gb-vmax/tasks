# Bug Report

### Describe the bug

I'm experiencing an issue with nested container parsing in MDX documents. When working with deeply nested block-level elements (like lists within blockquotes, or nested blockquotes), the parser seems to exit containers prematurely or incorrectly handle continuation checks.

### Reproduction

```mdx
> This is a blockquote
> - with a list item
> - and another item
>
> Still in the blockquote
```

Or with nested structures:

```mdx
> Outer blockquote
> > Inner blockquote
> > Still inner
> Back to outer
```

The parser appears to be closing containers when it should continue them, or vice versa. This affects how the document structure is built and can lead to incorrect AST generation.

### Expected behavior

The parser should correctly maintain the container stack and properly determine when to continue existing containers versus exiting them. Nested structures should be parsed with the correct hierarchy preserved.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

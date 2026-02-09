# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the order of processing seems to have changed. After a recent update, MDX content is not being parsed correctly - specifically, markdown elements appear to be processed before JSX expressions, which causes unexpected behavior in my documents.

### Reproduction

```mdx
# Hello {name}

This is a paragraph with {variable}.

<CustomComponent prop={value} />
```

When this MDX is processed, the expressions and JSX components are not being handled in the expected order. The markdown transformation seems to be interfering with the JSX/expression parsing.

### Expected behavior

MDX should parse expressions and JSX components correctly within markdown content. The processing order should allow JSX and expressions to be evaluated properly before markdown transformations are applied.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

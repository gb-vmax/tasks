# Bug Report

### Describe the bug

Variable declarations are not being parsed correctly in MDX files. When trying to use variable statements in MDX content, the parser seems to be processing tokens in the wrong order and returning an incorrect node type.

### Reproduction

```mdx
---
title: Test
---

export const myVariable = 'test value';

# My Content

{myVariable}
```

When parsing this MDX file, the variable declaration doesn't work as expected. The content either fails to render or the variable is not accessible in the component.

### Expected behavior

Variable declarations should be parsed correctly and the variables should be usable within the MDX content. The parser should properly handle the token sequence and return the correct AST node type for variable statements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with nested container parsing in MDX documents. When working with deeply nested container structures (like nested blockquotes or lists), the parser seems to be checking container continuation incorrectly, which causes unexpected behavior in document flow processing.

### Reproduction

```mdx
> First level blockquote
> > Second level blockquote
> > > Third level blockquote
> > > Content here

Additional content
```

When parsing documents with multiple levels of nested containers, the flow doesn't continue properly. The issue appears to be related to how the parser determines whether to continue with existing containers or check for new ones.

### Expected behavior

The parser should correctly handle nested containers at any depth level. When the continuation count matches or exceeds the stack length, it should properly determine whether to continue with the document flow or start checking for new containers.

Currently, the logic seems inverted - it's checking for `childFlow` existence when it should be checking for its absence, which breaks the control flow for nested container structures.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This is affecting production parsing of MDX documents with nested structures. Any help would be appreciated!

---
Repository: /testbed

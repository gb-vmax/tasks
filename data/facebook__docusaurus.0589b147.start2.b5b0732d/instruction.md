# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where the parser seems to be exiting states in the wrong order. This causes problems when parsing MDX expressions in certain edge cases.

### Reproduction

```mdx
{/* Simple expression */}
{someVariable}

{/* More complex expression */}
{user.profile.name}
```

When parsing MDX files with expressions, the tokenizer appears to be closing markers and types prematurely, which can lead to incorrect parsing state transitions.

### Expected behavior

The MDX expression parser should properly maintain state by exiting markers before exiting the parent type. The current behavior seems to exit the type before properly handling the marker exit, which breaks the state machine flow.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to affect the `factoryMdxExpression` function specifically when it processes the opening markers of MDX expressions.

---
Repository: /testbed

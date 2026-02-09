# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX flow tag parsing where the token types appear to be in the wrong order. When parsing JSX components in MDX, the tokens for tag name parts are being assigned incorrectly, which causes problems with syntax highlighting and AST generation.

### Reproduction

```mdx
<MyComponent.SubComponent prop="value" />
```

When parsing this component, the token types for `mdxJsxFlowTagNamePrimary` and `mdxJsxFlowTagNameMemberMarker` seem to be swapped in the internal parser configuration. This affects how the component name is tokenized.

### Expected behavior

The parser should correctly identify and tokenize the primary tag name and member marker in the proper sequence. The token type order should match the actual parsing order of JSX tag elements.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

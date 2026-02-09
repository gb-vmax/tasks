# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow tag parsing where the tag name is not being recognized correctly. It seems like the parser is treating the tag name as if it were an attribute value expression instead of properly identifying it as the primary tag name.

### Reproduction

```mdx
<MyComponent />
```

When parsing JSX flow tags in MDX, the component name `MyComponent` is being misidentified during tokenization. The parser appears to be applying the wrong token type to the tag name portion of the JSX syntax.

This affects any MDX file that uses custom component tags at the flow level (block-level components).

### Expected behavior

The parser should correctly identify and tokenize the tag name as `mdxJsxFlowTagNamePrimary` rather than confusing it with attribute-related tokens. The component should be parsed successfully and the tag name should be properly recognized.

### Additional context

This appears to affect the core tokenization logic for MDX JSX flow elements. The issue manifests when the parser processes the opening tag marker and attempts to classify the subsequent tokens.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where JSX flow elements aren't being recognized correctly. It seems like the parser is incorrectly handling the logic for detecting when to start parsing JSX elements vs. MDX expressions.

### Reproduction

```mdx
<Component>
  Some content here
</Component>

{/* This should work */}
{expression}
```

When parsing the above MDX content, the JSX elements that start with `<` are not being processed as expected. The parser appears to be applying the wrong condition check when determining whether to parse JSX flow vs. expressions.

### Expected behavior

The parser should correctly identify and parse JSX elements that begin with `<` (code 60) and handle MDX flow expressions that begin with `{` (code 123) separately. Currently, it seems like these conditions are inverted or incorrectly evaluated.

### System Info
- @mdx-js/mdx version: 3.0.0
- The issue appears to be in the `jsxFlow` function's `end` handler

---
Repository: /testbed

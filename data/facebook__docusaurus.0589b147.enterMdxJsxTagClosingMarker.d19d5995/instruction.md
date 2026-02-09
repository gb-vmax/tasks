# Bug Report

### Describe the bug

I'm encountering an issue with nested MDX JSX tags where the parser is incorrectly throwing an error for valid closing tags. When I have multiple levels of nested JSX components, the closing tag for an inner component triggers an unexpected error about a closing slash.

### Reproduction

```mdx
<Outer>
  <Inner>
    Content here
  </Inner>
</Outer>
```

When parsing the above MDX content, the closing tag `</Inner>` incorrectly raises an error:
```
Unexpected closing slash `/` in tag, expected an open tag first
```

This happens specifically when there are nested JSX tags. Single-level tags work fine, but as soon as you nest components, the parser gets confused about the tag stack.

### Expected behavior

The parser should correctly handle nested JSX tags and allow proper closing tags for inner components. The closing `</Inner>` tag should be recognized as valid since there's a matching opening `<Inner>` tag.

### Additional context

This seems to be related to how the tag stack is being validated. The error is thrown even though the tag structure is completely valid and properly nested.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag matching where closing tags with mismatched names are not being properly validated. When I have nested JSX tags in my MDX file and accidentally use the wrong closing tag, the parser doesn't throw an error as expected.

### Reproduction

```mdx
<Outer>
  <Inner>
    Content here
  </Inner>
</Wrong>
```

In the example above, the closing tag `</Wrong>` doesn't match the opening tag `<Outer>`, but the parser seems to be handling this incorrectly. The error message that should be thrown for mismatched tags is not appearing.

### Expected behavior

The parser should throw a `VFileMessage` error indicating that the closing tag `</Wrong>` is unexpected and that it expected a corresponding closing tag for `<Outer>`. The error should include the position information for both tags.

### Additional context

This appears to be related to the tag stack management in the MDX JSX parser. The validation logic for matching opening and closing tags seems to have an issue with the conditional checks.

---
Repository: /testbed

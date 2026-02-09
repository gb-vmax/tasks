# Bug Report

### Describe the bug

I'm encountering an issue with JSX flow tags in MDX where the parser is incorrectly handling whitespace and tag continuation logic. After recent changes, the parser seems to be applying inverted conditions when checking for markdown spaces and angle brackets (`<`), which causes JSX flow tags to be parsed incorrectly.

### Reproduction

```mdx
<MyComponent>
  Content here
</MyComponent>

<AnotherComponent />
```

When parsing the above MDX content, the JSX flow tags are not being recognized properly. The parser appears to be making incorrect decisions about when to continue parsing tags vs. when to end parsing.

### Expected behavior

JSX flow tags should be parsed correctly with proper whitespace handling. The parser should:
1. Correctly identify when whitespace follows a tag
2. Properly handle the continuation of tag parsing when encountering `<` characters
3. Parse both self-closing and regular JSX tags without errors

### Additional context

This seems related to the logic that determines whether to continue parsing after a JSX tag is encountered. The conditions for checking markdown spaces and angle brackets appear to be behaving opposite to what they should be doing.

---
Repository: /testbed

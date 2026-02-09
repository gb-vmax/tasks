# Bug Report

### Describe the bug

I'm encountering an issue with nested JSX tags in MDX files. When I have self-closing tags nested within other tags, the parser is throwing an error about an unexpected closing slash even though the syntax is valid.

### Reproduction

```mdx
<Wrapper>
  <Component />
</Wrapper>
```

When parsing the above MDX content, I get an error:
```
Unexpected closing slash `/` in tag, expected an open tag first
```

The error occurs on the self-closing `<Component />` tag even though it's properly nested inside the `<Wrapper>` tag.

### Expected behavior

The parser should correctly handle self-closing JSX tags that are nested within other JSX tags. This is valid JSX/MDX syntax and should parse without errors.

### Additional context

This appears to be related to how the tag stack is being managed during parsing. The issue only occurs when there are nested tags - standalone self-closing tags work fine:

```mdx
<Component />
```

This parses correctly without any issues.

---
Repository: /testbed

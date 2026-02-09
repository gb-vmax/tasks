# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX text tag parsing where malformed or invalid JSX syntax is being accepted without proper error handling. It seems like the parser is not correctly rejecting invalid JSX constructs in inline/text contexts.

### Reproduction

When I write invalid JSX syntax in an MDX file like:

```mdx
This is some text with <Component prop= /> invalid syntax.
```

or

```mdx
Text with <Component attr="unclosed > more text
```

The parser doesn't properly reject these malformed tags and continues processing as if they were valid. This can lead to unexpected output or silent failures in the parsing pipeline.

### Expected behavior

The parser should properly validate JSX syntax in text contexts and reject malformed tags with appropriate error messages, similar to how it handles other invalid JSX constructs.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

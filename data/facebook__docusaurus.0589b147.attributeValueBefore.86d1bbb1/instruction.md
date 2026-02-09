# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where quoted attribute values (using double quotes or single quotes) are not being recognized properly. When I try to use standard JSX-style attributes with quoted strings, the parser throws an error saying it expected a valid attribute value character.

### Reproduction

```mdx
<Component name="test" />
```

or

```mdx
<Component name='test' />
```

Both of these fail to parse. The parser seems to reject the quoted strings entirely and only accepts expression syntax with curly braces like `{...}`.

### Expected behavior

Standard JSX/MDX syntax with quoted attribute values should work correctly. Both double quotes and single quotes should be accepted for string attribute values, just like in regular JSX:

```mdx
<Component name="test" />
<Component name='test' />
```

These should parse without errors.

### System Info
- remark-mdx version: 3.0.0
- Node version: latest

This seems like a regression as quoted attributes are standard JSX syntax and should definitely be supported.

---
Repository: /testbed

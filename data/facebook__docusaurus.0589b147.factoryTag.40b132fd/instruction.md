# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing where JSX tags with attributes are not being recognized correctly. It seems like the parser is having trouble with closing quotes in attribute values and forward slashes in tag names.

### Reproduction

When trying to parse JSX tags with attributes in MDX content, the parser fails to properly handle:

1. Self-closing tags with forward slashes (e.g., `<Component />`)
2. Quoted attribute values with closing quotes

Example MDX content that's causing issues:

```mdx
<MyComponent name="test" />

<div className="container">
  <span title="hello">Content</span>
</div>
```

The parser seems to be treating these constructs incorrectly, particularly around:
- The forward slash in self-closing tags
- The closing quotes in attribute values like `name="test"`

### Expected behavior

The MDX parser should correctly recognize and parse:
- Self-closing JSX tags with the `/` character
- Attribute values enclosed in quotes (both opening and closing quotes should be matched)

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to use standard JSX syntax in MDX files. Any help would be appreciated!

---
Repository: /testbed

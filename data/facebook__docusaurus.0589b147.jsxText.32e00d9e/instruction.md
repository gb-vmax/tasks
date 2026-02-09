# Bug Report

### Describe the bug

I'm encountering an issue when parsing MDX content with JSX text tags. The parser seems to be failing or producing incorrect results when processing inline JSX components in MDX files.

### Reproduction

```mdx
Here is some text with <Component prop="value" /> inline JSX.

And another example: <AnotherComponent attribute="test">content</AnotherComponent>
```

When parsing this MDX content, the JSX text tags are not being recognized correctly. The parser either throws an error or produces malformed output.

### Expected behavior

The parser should correctly identify and process inline JSX components within MDX text content. Attributes should be properly parsed and the component structure should be maintained.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

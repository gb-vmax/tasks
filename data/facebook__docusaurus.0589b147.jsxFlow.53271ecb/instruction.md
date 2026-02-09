# Bug Report

### Describe the bug

I'm experiencing an issue with JSX flow tag parsing in MDX content. When JSX tags are followed by certain characters, the parser seems to behave incorrectly and doesn't handle the content as expected.

### Reproduction

```mdx
<MyComponent />
<AnotherComponent />
```

When I have JSX flow tags like this, the parsing appears to break down. The issue seems related to how whitespace and subsequent characters are being processed after a JSX tag closes.

I noticed this started happening recently and it's affecting how my MDX documents are being parsed. The parser seems to be making incorrect decisions about what comes after a JSX tag.

### Expected behavior

JSX flow tags should be parsed correctly regardless of what follows them (whitespace, other tags, line endings, etc.). The parser should properly recognize when a tag ends and continue parsing the rest of the document.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with footnote definitions in GitHub Flavored Markdown parsing. When processing footnotes, the parser seems to be leaving some internal state unclosed, which causes problems with subsequent parsing or when trying to serialize the syntax tree.

### Reproduction

```js
const input = `
[^1]: This is a footnote definition
with continuation

Some text referencing the footnote[^1]
`;

// Parse the markdown
const tree = processor.parse(input);
```

After parsing markdown with footnote definitions, the resulting syntax tree appears to be malformed or incomplete. The footnote definition tokens don't seem to be properly closed/exited.

### Expected behavior

Footnote definitions should be properly parsed and all internal tokens should be correctly opened and closed, resulting in a well-formed syntax tree that can be processed and serialized without issues.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed

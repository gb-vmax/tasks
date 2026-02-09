# Bug Report

### Describe the bug

HTML closing tags are not being parsed correctly in markdown content. When trying to use HTML tags in markdown, closing tags fail to be recognized properly, which breaks the rendering of HTML elements.

### Reproduction

```js
const markdown = `
<div>
  <p>Some content</p>
</div>
`;

// Process the markdown
const result = remark().processSync(markdown);
// The closing tags are not handled correctly
```

### Expected behavior

HTML closing tags should be properly tokenized and recognized when processing markdown content. Valid HTML structures with opening and closing tags should parse without issues.

### System Info
- remark version: 15.0.1
- Node version: Latest

The issue seems to affect any markdown content that includes HTML closing tags. The parser appears to reject valid closing tag syntax.

---
Repository: /testbed

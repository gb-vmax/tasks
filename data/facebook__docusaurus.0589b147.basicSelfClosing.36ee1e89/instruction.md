# Bug Report

### Describe the bug

I'm encountering a critical issue with HTML parsing in markdown content. When trying to parse markdown that contains self-closing HTML tags, the parser crashes or produces unexpected results. This appears to be causing problems with basic HTML elements in markdown documents.

### Reproduction

```js
const markdown = `
# Test Document

<img src="test.png" />

Some text here.
`;

// Parser fails to handle the self-closing img tag correctly
const result = remark().parse(markdown);
```

Also happens with other self-closing tags:
```markdown
<br />
<hr />
<input type="text" />
```

### Expected behavior

Self-closing HTML tags should be parsed correctly and the markdown processor should handle them without errors. The parser should recognize the `/>` syntax and properly close these tags.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

This is blocking our documentation pipeline as many of our markdown files contain self-closing HTML tags for images and other elements. Any help would be appreciated!

---
Repository: /testbed

# Bug Report

### Describe the bug

HTML closing tags are not being parsed correctly. When trying to parse markdown with HTML closing tags, they're being rejected even when they contain valid alphabetic characters.

### Reproduction

```js
const markdown = `
<div>
  Some content
</div>
`;

// Parse the markdown
const result = remark().parse(markdown);
```

The closing tag `</div>` is not being recognized properly. It seems like the parser is rejecting valid alphabetic characters in closing tags instead of accepting them.

### Expected behavior

HTML closing tags with alphabetic characters (like `</div>`, `</span>`, `</p>`, etc.) should be parsed correctly. The parser should accept alphabetic characters after the `</` sequence.

### System Info
- remark version: 15.0.1

---
Repository: /testbed

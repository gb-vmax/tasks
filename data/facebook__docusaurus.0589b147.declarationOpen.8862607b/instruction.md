# Bug Report

### Describe the bug

HTML comment parsing is broken in markdown files. When trying to parse markdown that contains HTML comments or declarations, the parser throws an error or fails to process the content correctly.

### Reproduction

```js
const markdown = `
Some text here

<!-- This is a comment -->

More text
`

// Parser fails to handle this correctly
const result = remark.parse(markdown)
```

Also fails with CDATA sections:
```js
const markdown = `<![CDATA[some data]]>`
```

And with HTML declarations:
```js
const markdown = `<!DOCTYPE html>`
```

### Expected behavior

The parser should correctly handle HTML comments, CDATA sections, and HTML declarations within markdown content. These are valid HTML constructs that should be parsed without errors.

### System Info
- remark version: 15.0.1

---
Repository: /testbed

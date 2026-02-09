# Bug Report

### Describe the bug

HTML tags in markdown are not being parsed correctly. When I try to use basic HTML elements in my markdown content, they either get stripped out or cause the parser to fail silently.

### Reproduction

```js
const markdown = `
<div>
  <p>Hello world</p>
</div>
`

// Parser fails to recognize the HTML tags
const result = remark().parse(markdown)
```

Also happens with self-closing tags:

```js
const markdown = `Some text <br/> more text`
// The <br/> tag is not handled properly
```

### Expected behavior

HTML tags should be recognized and parsed as valid HTML nodes within the markdown content. Both opening tags and self-closing tags should work as expected.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed

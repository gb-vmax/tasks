# Bug Report

### Describe the bug

HTML tags in markdown are not being parsed correctly. When I try to use HTML tags in my markdown content, they're either not recognized at all or cause the parser to fail unexpectedly.

### Reproduction

```js
const markdown = `
<div>
  <p>Hello world</p>
</div>
`;

// Parser fails to recognize the HTML tags
const result = remark.parse(markdown);
```

Also happens with self-closing tags:

```js
const markdown = `<img src="test.png" />`;
// Not parsed correctly
```

### Expected behavior

HTML tags should be properly recognized and parsed as HTML nodes in the markdown AST. Both opening tags with alphanumeric characters and self-closing tags should work.

### Additional context

This seems to affect various HTML elements including divs, spans, and other common tags. The parser appears to reject valid HTML that should be allowed in markdown documents.

---
Repository: /testbed

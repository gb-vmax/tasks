# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown link titles. When I try to parse links with quoted titles, the parser seems to hang or enter an infinite loop and never completes.

### Reproduction

```js
const markdown = `[link text](url "title here")`;

// Parser hangs when processing this
const result = remark.parse(markdown);
```

The same issue occurs with single quotes:
```js
const markdown = `[link text](url 'title here')`;
```

### Expected behavior

The parser should successfully parse the link and extract the title without hanging. It should return a valid AST with the link node containing the title information.

### Additional context

This seems to affect any markdown link that includes a title attribute. Links without titles parse fine:
```js
// This works fine
const markdown = `[link text](url)`;
```

The issue appears to be related to how the parser processes the quoted title strings. It gets stuck during the parsing phase and never returns.

---
Repository: /testbed

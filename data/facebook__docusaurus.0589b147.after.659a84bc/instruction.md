# Bug Report

### Describe the bug
Setext headings (underlined with `===` or `---`) are not being parsed correctly. When trying to parse markdown content with setext-style headings, the parser fails to recognize them properly and produces incorrect output.

### Reproduction
```js
const markdown = `
My Heading
==========

Some content here.

Another Heading
---------------

More content.
`;

// Parse the markdown
const result = remark().parse(markdown);

// The setext headings are not recognized correctly
console.log(result);
```

### Expected behavior
The parser should correctly identify setext headings and convert them to heading nodes. Both `===` and `---` underlines should work for creating h1 and h2 headings respectively.

### Additional context
This seems to affect all setext-style headings in the document. ATX-style headings (with `#` symbols) still work fine, but setext headings either fail to parse or produce unexpected results.

---
Repository: /testbed

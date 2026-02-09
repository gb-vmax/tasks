# Bug Report

### Describe the bug

Character references in markdown are not being parsed correctly. When processing markdown text with HTML entities or numeric character references (like `&amp;`, `&#x20;`, or `&#32;`), the parser appears to exit prematurely and doesn't properly handle the reference content.

### Reproduction

```js
const markdown = 'Text with &amp; entity';
const result = remark().parse(markdown);
// The character reference is not parsed correctly
```

Another example:
```js
const markdown = 'Unicode: &#x1F600;';
const result = remark().parse(markdown);
// Numeric character references are broken
```

### Expected behavior

Character references should be fully parsed, including:
- Named entities like `&amp;`, `&lt;`, `&gt;`
- Decimal numeric references like `&#65;`
- Hexadecimal numeric references like `&#x41;`

The parser should continue processing after encountering the opening `&` marker and properly handle the reference type (named vs numeric) before completing.

### System Info
- remark version: 15.0.1

---
Repository: /testbed

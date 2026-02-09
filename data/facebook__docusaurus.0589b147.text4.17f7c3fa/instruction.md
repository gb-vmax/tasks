# Bug Report

### Describe the bug

I'm encountering an issue with the remark markdown parser where text nodes are being created with incorrect properties. Specifically, text nodes appear to have a `null` value and reference an undefined `textType` variable instead of using the string literal `"text"`.

### Reproduction

When parsing markdown content that contains text nodes, the parser creates malformed text node objects:

```js
// Expected text node structure:
{
  type: "text",
  value: ""
}

// Actual text node structure being created:
{
  type: textType,  // undefined variable
  value: null      // should be empty string
}
```

This causes issues when trying to process or serialize the AST, as the text nodes don't have the expected structure.

### Expected behavior

Text nodes should be created with:
- `type` property set to the string `"text"`
- `value` property initialized to an empty string `""`

### System Info
- remark version: 15.0.1
- Node.js version: Latest

This seems to have been introduced in a recent change to the `text4()` function. The text node factory should return a properly structured object with correct type and value properties.

---
Repository: /testbed

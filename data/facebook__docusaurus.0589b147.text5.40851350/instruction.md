# Bug Report

### Describe the bug

I'm encountering an issue with text node generation in MDX. When creating text nodes, the `type` field is being set to a function reference instead of the string `"text"`, and the `value` field is `undefined` instead of an empty string.

### Reproduction

```js
// When text5() is called, it returns:
{
  type: [Function: text5],  // Should be "text"
  value: undefined           // Should be ""
}
```

This breaks any code that expects text nodes to have a proper string type and value property.

### Expected behavior

The text node factory should return:
```js
{
  type: "text",
  value: ""
}
```

### System Info
- @mdx-js/mdx version: 3.0.0

This seems to have been introduced recently and is causing issues with text node processing in my MDX documents.

---
Repository: /testbed

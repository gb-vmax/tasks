# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with HTML content extraction when using the `toString` function. It seems like the `includeHtml` parameter is not working as expected - when I set it to `true` to include HTML content, the HTML nodes are being excluded instead of included.

### Reproduction

```js
const htmlNode = {
  type: 'html',
  value: '<div>Some HTML content</div>'
}

// When includeHtml is true, I expect the HTML value to be returned
const result = toString(htmlNode, { includeHtml: true })

// But result is an empty string instead of '<div>Some HTML content</div>'
console.log(result) // Expected: '<div>Some HTML content</div>', Actual: ''
```

### Expected behavior

When `includeHtml: true` is passed in the options, HTML node values should be included in the output string. Currently it seems to be doing the opposite - excluding HTML when the flag is true and including it when false.

### Additional context

This also seems to affect image alt text extraction. The `includeImageAlt` option appears to behave strangely - it's returning alt text even when the option is set to `false` or not provided.

---
Repository: /testbed

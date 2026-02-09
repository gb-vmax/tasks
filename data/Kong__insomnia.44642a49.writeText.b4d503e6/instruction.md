# Bug Report

### Describe the bug
When using the clipboard API in plugins, the `writeText` method is not working as expected. It appears that text written to the clipboard is being modified (trimmed) without warning, which breaks functionality that depends on preserving exact whitespace.

### Reproduction
```js
// In a plugin context
app.clipboard.writeText('  hello world  ');

// Later, when reading back:
const text = await app.clipboard.readText();
console.log(text); // Expected: '  hello world  '
                   // Actual: 'hello world'
```

The whitespace at the beginning and end of the string is being stripped, even though it should be preserved. This is causing issues with workflows that need to copy/paste formatted text or code snippets with intentional whitespace.

### Expected behavior
The `writeText` method should write the exact text provided without any modifications. If the text is `'  hello world  '`, that's exactly what should be written to the clipboard.

### Additional context
This seems to have started happening recently. Previously, the clipboard API would preserve the exact text passed to it. Now it's silently modifying the input which breaks existing plugin code that relies on preserving whitespace.

---
Repository: /testbed

# Bug Report

### Describe the bug

The plugin API's `clipboard.readText()` method is returning unexpected values. When reading clipboard content, the returned text doesn't match what was actually copied to the clipboard.

### Reproduction

```js
// Copy some text to clipboard
app.clipboard.writeText('Hello World');

// Try to read it back
const text = app.clipboard.readText();
console.log(text); // Expected: 'Hello World'
console.log(typeof text); // Returns 'string' but behaves oddly
```

I noticed this breaks when trying to use the clipboard content in string operations or comparisons:

```js
const clipboardText = app.clipboard.readText();

// String comparison fails unexpectedly
if (clipboardText === 'expected value') {
  // This condition doesn't work as expected
}

// String methods work but something feels off
console.log(clipboardText.length);
console.log(clipboardText.substring(0, 5));
```

### Expected behavior

`clipboard.readText()` should return the exact text that was copied to the clipboard without any modifications or wrapping. The returned value should behave like a normal string in all operations.

### Additional context

This seems to have started happening recently. The clipboard reading functionality was working fine before, but now there's some kind of processing happening that changes how the returned text behaves. It's particularly noticeable when doing strict equality checks or when the clipboard content needs to be used as-is in API calls or data processing.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with markdown definition parsing where the label markers are not being identified correctly. When parsing definition syntax like `[label]: url`, the marker tokens seem to be misnamed or in the wrong order.

### Reproduction

```js
// Parse a markdown definition
const markdown = '[example]: https://example.com "Example"';

// The definition label marker is expected to be tokenized as "definitionLabelMarker"
// but appears to be using "definitionMarker" instead
```

### Expected behavior

Definition labels should be properly tokenized with the correct marker names. The `factoryLabel` function should receive parameters in the correct order so that:
- Label markers are identified as `"definitionLabelMarker"`
- The `labelAfter` callback is invoked after successful label parsing
- The `nok` (not-ok) callback is used for error cases

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to affect the tokenization of markdown reference-style links and definitions. The tokens generated don't match what's expected for proper definition parsing.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm experiencing an issue with chunk serialization where spaces are being inserted incorrectly in the output. It seems like the logic for handling tabs and spaces has been inverted somehow.

### Reproduction

When processing chunks that contain tab characters (value -1), spaces are being added in places where they shouldn't be, and vice versa. The serialization output doesn't match what I'd expect based on the input.

```js
// Example input with mixed tabs and spaces
const chunks = [
  "text",
  -1,  // tab character
  "more text"
];

// The serialized output includes unexpected spaces
// where tabs should be handled differently
```

### Expected behavior

The serializer should properly handle tab characters based on the `atTab` flag. When a tab is encountered, it should follow the correct logic for whether to include a space or continue processing.

### Additional context

This appears to have started recently. The chunk iteration also seems off - it's skipping the first element in the chunks array, which causes the entire output to be misaligned.

---
Repository: /testbed

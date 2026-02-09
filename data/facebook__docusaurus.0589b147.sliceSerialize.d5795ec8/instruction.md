# Bug Report

### Bug with token serialization in MDX parser

I'm encountering an issue with the MDX parser where token serialization seems to be producing incorrect output. The problem appears to be related to how tokens are being processed when `expandTabs` is involved.

### Reproduction

```js
const token = {
  type: 'text',
  start: 0,
  end: 10
}

// Serializing tokens with expandTabs option
const result = sliceSerialize(token, true)

// Getting unexpected output format
console.log(result) // Not getting the expected serialized string
```

### Expected behavior

The `sliceSerialize` function should properly serialize token chunks and handle the `expandTabs` parameter correctly. The serialized output should match the token's content from the stream.

### Additional context

This seems to affect how the tokenizer processes and serializes content. The order of operations between slicing the stream and serializing chunks might be incorrect, leading to malformed output.

---
Repository: /testbed

# Bug Report

### Describe the bug
I'm experiencing an issue with markdown parsing where the serialization of tokens is producing incorrect output. It seems like the token stream is not being properly sliced before serialization, which causes the serializer to receive the wrong data.

### Reproduction
```js
const parser = createMarkdownParser();
const token = parser.tokenize('some **bold** text');

// When serializing the token, the output doesn't match the expected format
const serialized = sliceSerialize(token, true);
console.log(serialized); // Output is incorrect
```

### Expected behavior
The `sliceSerialize` function should properly slice the token stream and then serialize it. The serialized output should accurately represent the original token content.

### Additional context
This appears to be related to how tokens are being processed internally. The sliced stream should be passed to the serializer, but it seems like the wrong data is being used instead.

---
Repository: /testbed

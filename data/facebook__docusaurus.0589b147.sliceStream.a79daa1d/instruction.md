# Bug Report

### Describe the bug

I'm experiencing an issue with token serialization in the MDX parser. When trying to serialize tokens, I'm getting unexpected `undefined` or `null` values instead of the actual token stream content.

### Reproduction

```js
const token = {
  type: 'text',
  start: { line: 1, column: 1, offset: 0 },
  end: { line: 1, column: 5, offset: 4 }
}

// Attempting to slice the token stream
const result = sliceStream(token)
// Expected: chunks sliced from the token
// Actual: undefined or null
```

### Expected behavior

The `sliceStream` function should return the proper chunk slices based on the provided token. The token object should be passed correctly to `sliceChunks` so that the serialization works as intended.

### Additional context

This seems to be affecting MDX parsing when working with token streams. The serialized output is not what's expected, and it looks like the token information is being lost somewhere in the process.

---
Repository: /testbed

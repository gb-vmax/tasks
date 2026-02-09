# Bug Report

### Describe the bug

I'm experiencing an issue with environment variable rendering where the first element of arrays is being skipped. When I have an array in my environment variables, the element at index 0 is not being processed correctly, but all subsequent elements work fine.

### Reproduction

```js
// Environment variable setup
{
  "myArray": [
    "first",
    "second", 
    "third"
  ]
}

// When accessing the array elements:
// myArray[0] -> not available/not rendered
// myArray[1] -> works correctly
// myArray[2] -> works correctly
```

The first element seems to be completely ignored during the rendering process, while elements at index 1 and beyond are processed as expected.

### Expected behavior

All array elements including the first one (index 0) should be rendered and accessible. The element at `myArray[0]` should return `"first"` just like `myArray[1]` returns `"second"`.

### System Info
- Insomnia version: latest
- OS: macOS

Has anyone else run into this? It's causing issues with my API requests that rely on the first element of arrays in environment variables.

---
Repository: /testbed

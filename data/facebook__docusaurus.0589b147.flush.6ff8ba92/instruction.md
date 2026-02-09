# Bug Report

### Describe the bug

I'm encountering an issue with entity parsing where the output seems to be missing content. When parsing text with HTML entities, the result array doesn't contain the expected text segments.

### Reproduction

```js
const result = parseEntities('Hello &amp; world', {
  text: (value, position) => {
    console.log('Text:', value);
  }
});

console.log(result); // Expected: ['Hello ', '&', ' world'] but getting empty strings
```

The text callback is being called correctly with the right values, but the final result array is not being populated as expected. It looks like the queue is being cleared before it's added to the result.

### Expected behavior

The `result` array should contain all the text segments that were processed, including the content that was passed to the text callback.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

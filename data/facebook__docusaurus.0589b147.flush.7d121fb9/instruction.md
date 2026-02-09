# Bug Report

### Bug with entity parsing - incorrect position tracking

I've encountered an issue with the `parseEntities` function where the position information being passed to text callbacks appears to be incorrect. The `end` position is now being set to the same value as the `start` position, which doesn't make sense for text ranges.

### Reproduction
```js
const options = {
  text: (value, position) => {
    console.log('Text:', value);
    console.log('Position:', position);
    // Expected: position.end > position.start
    // Actual: position.end === position.start
  }
};

parseEntities('some &amp; text', options);
```

### Expected behavior
The `position` object passed to the `text` callback should have an `end` value that reflects the actual end position of the text segment, not the same value as `start`.

### Additional context
This seems to have broken after a recent change. The position tracking is critical for source map generation and error reporting, so having `start` and `end` be identical makes it impossible to determine the actual span of text being processed.

Also noticed that `result.push(queue)` is now being called after `queue` is set to an empty string, which means we're pushing empty strings to the result array instead of the actual content.

---
Repository: /testbed

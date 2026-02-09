# Bug Report

### Describe the bug

The `createAbsoluteFilePathMatcher` function is not working correctly when matching file paths. Files that should be matched by the glob patterns are not being detected, and the relative path calculation seems to be producing incorrect results.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/home/user/project/docs']
);

// This should return true but returns false
const result = matcher('/home/user/project/docs/introduction.md');
console.log(result); // Expected: true, Actual: false
```

When trying to match files in a specific root folder, the matcher fails to recognize files that should match the glob pattern. It appears the relative path being passed to the underlying matcher is incorrect.

### Expected behavior

The matcher should correctly identify files that match the provided glob patterns within the specified root folders. The relative path should be calculated from the root folder to the file, not the other way around.

### Additional context

This seems to have started happening recently. The file path matching was working fine before but now files aren't being picked up by the glob patterns even though they clearly should match.

---
Repository: /testbed

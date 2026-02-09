# Bug Report

### Describe the bug

I'm encountering an issue where duplicate exports in MDX files are not being detected properly. When I have the same export name declared multiple times, the parser isn't raising an error as expected.

### Reproduction

```js
export const foo = 1;
export const foo = 2;  // Should raise "Duplicate export 'foo'" error but doesn't
```

The code above should throw a duplicate export error, but it's being silently accepted. This allows invalid MDX files to pass through without any warnings.

### Expected behavior

The parser should raise a recoverable error with the message "Duplicate export 'foo'" when encountering duplicate export declarations. This is critical for catching potential bugs in MDX files where the same export name is accidentally used twice.

### Additional context

This seems to affect all types of exports (named exports, default exports, etc.). The duplicate detection mechanism appears to be inverted - it's only checking exports that haven't been seen before rather than ones that have already been registered.

---
Repository: /testbed

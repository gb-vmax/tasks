# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When I include metadata after the language identifier in a code fence, the parser seems to enter an infinite loop or hang indefinitely.

### Reproduction

```markdown
```javascript some-metadata
console.log('hello');
```
```

When parsing the above markdown with a fenced code block that has metadata after the language identifier, the parser hangs and doesn't complete.

### Expected behavior

The parser should correctly handle code fences with metadata and parse them without hanging. The metadata should be recognized as part of the fence definition and the code block should be processed normally.

### Additional context

This seems to affect any fenced code block where metadata is present after the language identifier. Simple code blocks without metadata work fine:

```markdown
```javascript
console.log('works fine');
```
```

The issue appears to be related to how the parser handles the transition from the language info to the metadata section of the fence.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX. When using backticks (```) to create code blocks, the parser seems to be accepting code blocks that should be invalid. Specifically, code fence info strings that contain backtick characters matching the fence marker are being parsed when they should be rejected.

### Reproduction

```markdown
```javascript`
console.log('test');
```
```

The above should fail to parse because the info string contains a backtick that matches the fence marker, but it's being accepted as valid MDX.

Also, code blocks that should terminate properly at the end of input are now behaving unexpectedly - they seem to continue parsing when they should stop.

### Expected behavior

According to the CommonMark spec, if the info string of a fenced code block contains a backtick character that matches the fence marker character, the code block should be invalid and not parse correctly. The parser should reject such constructs.

Additionally, code blocks should properly handle end-of-input scenarios and terminate correctly when reaching null/EOF.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

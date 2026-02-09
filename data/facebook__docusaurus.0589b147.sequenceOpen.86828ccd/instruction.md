# Bug Report

### Describe the bug

Code fences with exactly 3 backticks or tildes are not being recognized properly. The parser seems to reject valid fenced code blocks that should be accepted according to the CommonMark spec.

### Reproduction

```markdown
```js
console.log('test');
```
```

When parsing the above markdown with a standard 3-backtick fence, the code block is not properly tokenized. This affects both backticks (`) and tildes (~) as fence markers.

### Expected behavior

According to CommonMark specification, code fences should be recognized with a minimum of 3 consecutive fence characters. A fence with exactly 3 characters should create a valid code block.

The following should all be valid:
- ` ``` ` (3 backticks)
- `~~~` (3 tildes)  
- ` ```` ` (4 backticks)
- etc.

Currently it appears that only fences with 4+ characters are working correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed

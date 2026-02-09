# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where code blocks with exactly 3 backticks or tildes are not being recognized properly. The parser seems to be rejecting valid code fence sequences.

### Reproduction

```markdown
```javascript
console.log('hello');
```
```

The above code block (using exactly 3 backticks) is not being parsed correctly. It appears the fence sequence validation has changed and is now requiring more than 3 characters instead of at least 3.

### Expected behavior

According to the CommonMark spec, fenced code blocks should be delimited by at least 3 consecutive backticks (`) or tildes (~). A sequence of exactly 3 fence characters should be valid and properly recognized as a code block delimiter.

### Additional context

This appears to have started happening recently. Code blocks with 4 or more backticks work fine, but the standard 3-backtick fence is being rejected. This breaks a lot of existing MDX content that uses the standard triple-backtick syntax for code blocks.

---
Repository: /testbed

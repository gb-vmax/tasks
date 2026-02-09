# Bug Report

### Describe the bug

After a recent update, I'm unable to use short titles (1-2 characters) for prompt template tags. The validation now requires at least 3 characters, but I have existing workflows that use single-letter titles like "A", "B", "X", etc. for quick prompts.

### Reproduction

```js
// Create a prompt template tag with a short title
{
  title: 'A',  // Single character title
  label: 'Input A'
}

// Or with 2 characters
{
  title: 'AB',
  label: 'Input AB'
}
```

Both of these now fail validation with "Title must be at least 3 characters" error, even though they were working fine before.

### Expected behavior

Short titles (1-2 characters) should be allowed for prompt template tags. There's no technical reason why single-letter titles shouldn't work, and they're actually quite useful for simple, frequently-used prompts.

### Additional context

This is breaking my existing setup where I use single-letter prompts for common variables. Having to rename all of them to be 3+ characters is tedious and unnecessary.

---
Repository: /testbed

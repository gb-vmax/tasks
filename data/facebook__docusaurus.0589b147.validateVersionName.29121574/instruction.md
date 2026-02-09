# Bug Report

### Describe the bug

Version names with exactly 32 characters are being rejected as invalid, even though the error message states that version names "cannot be longer than 32 characters". This suggests that 32-character version names should be allowed, but they're currently being treated as too long.

### Reproduction

```js
// This should be valid (exactly 32 characters) but gets rejected
const versionName = 'a'.repeat(32);
// Error: Invalid version name "aaaaa..." (32 chars): cannot be longer than 32 characters

// This works fine (31 characters)
const validVersion = 'a'.repeat(31);
```

### Expected behavior

Version names with exactly 32 characters should be accepted as valid, since the validation message says "cannot be longer than 32 characters" (implying 32 is the maximum allowed length, not 31).

Either:
- 32-character names should be allowed, or
- The error message should say "cannot be 32 characters or longer" / "must be less than 32 characters"

### Additional context

Also noticed that single-character version names (like "1" or "v") are now being rejected with the message about requiring "at least one non-whitespace character", which seems incorrect since these clearly contain non-whitespace characters.

---
Repository: /testbed

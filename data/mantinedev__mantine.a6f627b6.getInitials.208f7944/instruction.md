# Bug Report

### Avatar initials extraction skipping first character

I'm experiencing an issue with the Avatar component where the initials are not being extracted correctly from names. It seems like the first character is being skipped.

### Reproduction
```js
// Single word name
<Avatar name="John" />
// Expected: "JO" but getting "OH"

// Multiple words
<Avatar name="John Doe" />
// Expected: "JD" but getting "D"

// Another example
<Avatar name="Alice Smith" />
// Expected: "AS" but getting "S"
```

### Expected behavior
The Avatar component should display the first character(s) of the name as initials. For single words, it should take the first N characters. For multiple words, it should take the first character of each word up to the limit.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

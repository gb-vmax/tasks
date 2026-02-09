# Bug Report

### Describe the bug

The Avatar component is showing incorrect initials when displaying user names. Instead of showing the first letter of each word, it's displaying the second character of each word.

### Reproduction

```js
import { Avatar } from '@mantine/core';

// Expected: "JD" but shows "oA" instead
<Avatar name="John Doe" />

// Expected: "AB" but shows "lO" instead  
<Avatar name="Alice Bob" />

// Expected: "JS" but shows "oM" instead
<Avatar name="Jane Smith" />
```

### Expected behavior

The Avatar component should display the first letter of each word in the name as initials. For example:
- "John Doe" should show "JD"
- "Alice Bob" should show "AB"
- "Jane Smith" should show "JS"

Currently it's picking the wrong character from each word.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed

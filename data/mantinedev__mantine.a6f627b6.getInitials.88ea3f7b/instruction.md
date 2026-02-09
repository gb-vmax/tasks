# Bug Report

### Describe the bug

The Avatar component is not displaying initials correctly. When I provide a single-word name, the first character is missing from the initials. For example, if I pass "John" as the name, I expect to see "JO" but instead I'm seeing something like "OH" or an empty string.

### Reproduction

```jsx
import { Avatar } from '@mantine/core';

// Single word name - initials are wrong
<Avatar name="John" />
// Expected: "JO" or "J"
// Actual: Shows incorrect characters or nothing

<Avatar name="Alice" />
// Expected: "AL" or "A"
// Actual: Shows "LI" or similar wrong characters
```

Also noticed that when using multiple words, I'm getting one extra initial than expected:

```jsx
<Avatar name="John Doe" />
// Expected: "JD" (2 initials by default)
// Actual: Shows 3 initials "JDX" or similar
```

### Expected behavior

- For single-word names, the Avatar should display the first character(s) of that name
- For multi-word names, it should display the first character of each word up to the specified limit
- The default limit should be 2 initials

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

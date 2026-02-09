# Bug Report

### Describe the bug

The Avatar component is displaying incorrect initials when a single-word name is provided. Instead of showing the first characters of the name, it's skipping the first character and showing characters starting from the second position.

### Reproduction

```jsx
import { Avatar } from '@mantine/core';

// This should show "JO" but shows "OH" instead
<Avatar name="John" />

// This should show "A" but shows "L" instead  
<Avatar name="Alice" />

// This should show "SA" but shows "AM" instead
<Avatar name="Sam" />
```

### Expected behavior

When passing a single-word name to the Avatar component, the initials should be taken from the beginning of the name. For example:
- "John" should display "JO"
- "Alice" should display "AL"  
- "Sam" should display "SA"

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

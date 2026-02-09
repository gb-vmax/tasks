# Bug Report

### Describe the bug

I'm experiencing an issue with style props in Mantine components where numeric values are being converted to strings unexpectedly. When I pass a number (like `0` or `false`) as a style prop value, it gets stringified instead of being treated as the original value type.

### Reproduction

```tsx
import { Box } from '@mantine/core';

// This renders "0" as a string instead of the numeric value 0
<Box style={{ opacity: 0 }}>Content</Box>

// Boolean false becomes string "false"
<Box style={{ display: false }}>Content</Box>

// Even numeric properties get converted
<Box style={{ zIndex: 0 }}>Content</Box>
```

When inspecting the computed styles, I see string values like `"0"` and `"false"` instead of the proper numeric/boolean types. This breaks CSS properties that expect specific value types.

### Expected behavior

Style prop values should maintain their original type. Numbers should remain numbers, booleans should remain booleans, and only actual string values should be strings. The resolver should pass through values as-is without converting them.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed

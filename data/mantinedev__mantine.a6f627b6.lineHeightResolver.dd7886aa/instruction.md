# Bug Report

### Describe the bug

When using the `lh` (line-height) style prop with theme values, the generated CSS variable is incorrect. Instead of referencing `--mantine-line-height-*`, it's generating `--mantine-font-size-*` which causes line heights to be completely wrong.

Additionally, when passing heading values like `'h1'`, `'h2'`, etc. to the line-height prop, they're not being resolved to the correct CSS variables.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This generates the wrong CSS variable
<Box lh="md">
  Some text with medium line height
</Box>

// Expected: var(--mantine-line-height-md)
// Actual: var(--mantine-font-size-md)

// Heading line heights also don't work
<Box lh="h1">
  Text that should use h1 line height
</Box>

// This doesn't resolve to var(--mantine-h1-line-height) as expected
```

### Expected behavior

- When using theme line-height values (xs, sm, md, lg, xl), the `lh` prop should generate `var(--mantine-line-height-{value})` CSS variables
- When using heading values (h1-h6), it should generate `var(--mantine-{heading}-line-height)` CSS variables
- Text should render with the correct line spacing based on the theme configuration

### System Info
- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed

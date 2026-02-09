# Bug Report

### Describe the bug

I'm experiencing an issue with responsive breakpoints not being applied in the correct order. It seems like the breakpoints are being processed in the wrong sequence, causing styles for larger screens to override those meant for smaller screens (or vice versa).

### Reproduction

```tsx
import { Container } from '@mantine/core';

function Demo() {
  return (
    <Container
      style={{
        // Breakpoint styles should be applied from smallest to largest
        // but they appear to be in wrong order
      }}
    >
      Content
    </Container>
  );
}
```

When I define multiple breakpoints like `xs`, `sm`, `md`, `lg`, the styles don't cascade properly. For example, a style meant for mobile (`xs`) might be overridden by tablet (`sm`) even when viewing on mobile.

### Expected behavior

Breakpoints should be sorted and applied in ascending order (smallest to largest) so that media queries work correctly and styles cascade as intended. The smaller breakpoint styles should be the base, with larger breakpoints overriding as needed.

### System Info

- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

This might be related to how breakpoints are being sorted internally. The order seems incorrect when multiple breakpoints are used together.

---
Repository: /testbed

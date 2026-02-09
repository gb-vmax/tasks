# Bug Report

### Describe the bug

The `useMantineIsHeadless()` hook is returning the opposite value of what it should. When headless mode is enabled, it returns `false`, and when headless mode is disabled, it returns `true`.

### Reproduction

```tsx
import { MantineProvider, useMantineIsHeadless } from '@mantine/core';

function TestComponent() {
  const isHeadless = useMantineIsHeadless();
  console.log('Is headless:', isHeadless);
  return <div>Check console</div>;
}

// With headless enabled
<MantineProvider theme={{}} headless>
  <TestComponent /> {/* Logs: Is headless: false (expected: true) */}
</MantineProvider>

// With headless disabled
<MantineProvider theme={{}}>
  <TestComponent /> {/* Logs: Is headless: true (expected: false) */}
</MantineProvider>
```

### Expected behavior

`useMantineIsHeadless()` should return `true` when the provider has `headless` prop set to `true`, and `false` otherwise.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

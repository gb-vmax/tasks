# Bug Report

### Describe the bug

When using `DatesProvider` to override default date settings, the custom settings are being ignored and the default values are used instead. It seems like the provider is not properly merging user-provided settings with defaults.

### Reproduction

```tsx
import { DatesProvider } from '@mantine/dates';

function App() {
  return (
    <DatesProvider settings={{ locale: 'fr', timezone: 'Europe/Paris' }}>
      {/* Components here use default locale/timezone instead of custom ones */}
    </DatesProvider>
  );
}
```

### Expected behavior

The custom `locale` and `timezone` settings should override the default values. Components wrapped in `DatesProvider` should respect the provided settings.

### Current behavior

The provider appears to be using default settings even when custom settings are explicitly provided. Custom locale and timezone configurations are not being applied to child components.

---
Repository: /testbed

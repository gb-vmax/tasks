# Bug Report

### Describe the bug

When using `DatesProvider` with custom settings, the default settings are overriding the custom settings instead of the other way around. For example, if I try to set a custom `locale` or `timezone`, the defaults take precedence and my custom values are ignored.

### Reproduction

```tsx
import { DatesProvider } from '@mantine/dates';

function App() {
  return (
    <DatesProvider settings={{ locale: 'fr', timezone: 'Europe/Paris' }}>
      {/* Components here will use default locale/timezone instead of 'fr' and 'Europe/Paris' */}
    </DatesProvider>
  );
}
```

### Expected behavior

Custom settings passed to `DatesProvider` should override the default settings, not be overridden by them. In the example above, the locale should be `'fr'` and timezone should be `'Europe/Paris'`.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed

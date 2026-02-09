# Bug Report

### Describe the bug

When using `DatesProvider` with custom settings, the provided settings are being ignored and default settings are always applied instead. This makes it impossible to override default date formatting, locale, or other date-related configurations.

### Reproduction

```jsx
import { DatesProvider } from '@mantine/dates';

function App() {
  return (
    <DatesProvider settings={{ locale: 'de', firstDayOfWeek: 1, weekendDays: [0, 6] }}>
      {/* Date components here - they still use default settings */}
    </DatesProvider>
  );
}
```

### Expected behavior

Custom settings passed to `DatesProvider` should override the default settings. For example, setting `locale: 'de'` should make all child date components use German locale instead of the default.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed

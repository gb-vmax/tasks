# Bug Report

### Describe the bug

When using `DatesProvider` with custom settings, the settings are being ignored and default values are used instead. This appears to be a regression as custom locale, timezone, and other date-related settings are not being applied to child components.

### Reproduction

```jsx
import { DatesProvider } from '@mantine/dates';

function App() {
  return (
    <DatesProvider settings={{ locale: 'de', firstDayOfWeek: 1, weekendDays: [0, 6] }}>
      <DatePicker />
    </DatesProvider>
  );
}
```

In this example, the DatePicker component should use the German locale and start weeks on Monday (firstDayOfWeek: 1), but instead it uses the default settings (English locale, Sunday as first day).

### Expected behavior

Custom settings passed to `DatesProvider` should override the default settings and be applied to all date components within the provider. The locale, firstDayOfWeek, weekendDays, and other custom configurations should work as documented.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

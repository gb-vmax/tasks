# Bug Report

### Describe the bug

When using `DatesProvider` with custom settings, the settings are not being applied correctly. It seems like the default settings are overriding my custom configuration instead of the other way around.

### Reproduction

```jsx
import { DatesProvider } from '@mantine/dates';

function App() {
  return (
    <DatesProvider
      settings={{
        locale: 'fr',
        firstDayOfWeek: 1,
        weekendDays: [0, 6],
        timezone: 'Europe/Paris'
      }}
    >
      {/* Date components here */}
    </DatesProvider>
  );
}
```

When I try to use custom settings like above, the date components still use the default settings. For example, the locale remains in English and the first day of week is not Monday as specified.

### Expected behavior

The custom settings passed to `DatesProvider` should override the default settings, allowing users to customize locale, first day of week, weekend days, timezone, etc.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed

# Bug Report

### Describe the bug

When using `DatesProvider` to set custom date settings, the provided settings are being overridden by default settings instead of the other way around. This means custom configurations like `locale`, `timezone`, or `firstDayOfWeek` are ignored and the component always uses the defaults.

### Reproduction

```jsx
import { DatesProvider } from '@mantine/dates';

// Try to set a custom locale and first day of week
<DatesProvider settings={{ locale: 'de', firstDayOfWeek: 1 }}>
  <YourDateComponent />
</DatesProvider>
```

The component inside still uses the default locale and firstDayOfWeek instead of the custom values passed to the provider.

### Expected behavior

Custom settings passed to `DatesProvider` should take precedence over default settings. When I specify a locale or firstDayOfWeek, those values should be used by child components, not the defaults.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed

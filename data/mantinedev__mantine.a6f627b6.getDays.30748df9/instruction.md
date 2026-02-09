# Bug Report

### Describe the bug

I'm experiencing an issue with the month component where it seems like only a single day button is being selected instead of all day buttons. The component is not rendering or selecting all the days in the month view properly.

### Reproduction

When rendering a month component with multiple days, only the first day button appears to be accessible/selected instead of all the day buttons in the table.

Expected: All day buttons in the month calendar should be selectable
Actual: Only one day button is being returned/selected

This seems to affect any component that displays a full month calendar view with multiple day buttons.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

Has anyone else encountered this? It's making it impossible to interact with all the days in the calendar.

---
Repository: /testbed

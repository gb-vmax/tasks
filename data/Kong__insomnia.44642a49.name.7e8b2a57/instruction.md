# Bug Report

### Describe the bug
I'm experiencing an issue with team name display in the sync functionality. When loading team information, the team name appears as "teamName" instead of the actual team name value. This seems to be affecting how team data is being processed or returned.

### Reproduction
```js
// When fetching team data
const team = getTeamData();
console.log(team.name); // Expected: actual team name, Got: "teamName"
```

The team name field is returning a literal string "teamName" rather than the actual name of the team. This is causing issues in the UI where all teams are showing up with the same generic label.

### Expected behavior
The team schema should return the actual team name value, not a string literal. Team names should be displayed correctly in the interface.

### System Info
- Insomnia version: latest
- Sync feature affected

---
Repository: /testbed

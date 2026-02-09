# Bug Report

### Describe the bug

When importing Postman environment files, disabled environment variables are being imported instead of enabled ones. The importer seems to have inverted logic - it's only including variables that are marked as disabled in the Postman environment file and skipping the enabled variables.

### Reproduction

1. Create a Postman environment with the following variables:
   - Variable 1: key="API_KEY", value="test123", enabled=true
   - Variable 2: key="DEBUG_MODE", value="false", enabled=false
2. Export the environment as a JSON file
3. Import the environment file into Insomnia
4. Check which variables were imported

### Expected behavior

Only the enabled variables (API_KEY in the example above) should be imported into the Insomnia environment. Disabled variables should be excluded from the import.

### Actual behavior

The disabled variables are being imported while the enabled ones are skipped. In the example above, only DEBUG_MODE gets imported, while API_KEY is missing from the imported environment.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when migrating from Postman since we have to manually go through and enable/disable the correct variables after import.

---
Repository: /testbed

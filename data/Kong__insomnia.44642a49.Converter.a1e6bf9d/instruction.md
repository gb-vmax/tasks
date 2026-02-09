# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with Swagger 2.0 imports in Insomnia. The import process seems to be incomplete or cutting off midway through, particularly when dealing with the base environment setup.

### Reproduction

When importing a Swagger 2.0 API specification file:

1. Open Insomnia
2. Try to import a valid Swagger 2.0 JSON/YAML file
3. The import appears to start but doesn't complete properly

The issue seems to affect the environment variables setup during import. The base environment data appears to be truncated or incomplete after the import finishes.

### Expected behavior

The Swagger 2.0 file should import completely with all environment variables and configuration properly set up. The base environment should contain the full `base_url` and any other necessary variables extracted from the API specification.

### Additional context

This worked fine in previous versions. The import process doesn't throw any errors, but the resulting workspace seems incomplete. It looks like the environment setup is being cut off during the conversion process.

---
Repository: /testbed

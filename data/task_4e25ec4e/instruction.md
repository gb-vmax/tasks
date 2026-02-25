You are helping an automation specialist organize workflow configurations. In the /home/user/workflows directory, there are two configuration files: one YAML file named "base_workflow.yaml" and one TOML file named "advanced_workflow.toml".

1. Edit "base_workflow.yaml" to add a new job under the "jobs" key. The new job should have:
   - A key called "deploy"
   - "runs-on" set to "ubuntu-22.04"
   - "steps" as a YAML list containing a single step with:
       - name: Print deployment
       - run: echo "Deploying application"

2. Edit "advanced_workflow.toml" to add a new section called [job.deploy]. Inside this section, set:
   - runs_on = "ubuntu-22.04"
   - [[job.deploy.steps]]
       - name = "Print deployment"
       - run = "echo 'Deploying application'"

Both configuration files must exactly match the following formats for their new entries:
- For YAML, indent with 2 spaces, and lists must use dash-and-space syntax.
- For TOML, use standard TOML section and table syntax, with no leading spaces or tabs for section headers.

When you have finished, create a new file /home/user/workflows/verification.log. In this log file, write the string "WORKFLOW CONFIGURATION: COMPLETE" (all uppercase, no quotes, single line).

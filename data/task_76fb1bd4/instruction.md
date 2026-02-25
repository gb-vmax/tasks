You are acting as a release manager who needs to prepare deployment manifests for a set of services before a new release. You are provided with a CSV file at /home/user/releases/service_list.csv, which contains the deployment information for each service. The CSV file has the following columns (with header): service_name, current_version, next_version, maintainer.

Your goal is to transform this data into individual YAML manifest files, one for each service, which will be used for deployment automation. For each row (except the header), generate a YAML file named /home/user/releases/deployments/&lt;service_name&gt;-deploy.yaml. Each YAML file should contain the following keys and structure:

service:
  name: &lt;service_name from CSV&gt;
  deploy_version: &lt;next_version from CSV&gt;
  maintainer: &lt;maintainer from CSV&gt;
  changelog: |
    Upgraded from &lt;current_version from CSV&gt; to &lt;next_version from CSV&gt; in this release.

All indentations must be 2 spaces (YAML standard). After generating all deployment YAML files, list the files in /home/user/releases/deployments and create a plain text log file at /home/user/releases/deployment_manifest.log. The log file should contain a list of the generated YAML filenames, one per line, sorted in ascending order.

The automated test will check that each deployment YAML follows the specified structure and indentation, the manifests are named correctly, and the log file lists all manifest files, sorted.

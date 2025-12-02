import datarobot as dr

# Initialize the DataRobot client
# This assumes you have a datarobot.yaml file or environment variables set up
dr.Client()

# Define the Use Case ID to associate the project with
use_case_id = "68f8035c957e8e82f4cc1b1f"

# List available DataSources and print those matching specific keywords
# This helps in finding the correct data source ID if unknown
for ds in dr.DataSource.list():
    if 'fraud' in ds.canonical_name.lower():
        print(ds.id, ds.canonical_name)
    if 'churn' in ds.canonical_name.lower():
        print(ds.id, ds.canonical_name)
    if 'lending' in ds.canonical_name.lower():
        print(ds.id, ds.canonical_name)

# Configuration for the project
data_source_id = "64c12903d08274d3bd214806" # ID of the data source to use
credential_id = "64c11792ed57dee5c1ed9cc0"  # ID of the credentials for the data source
target_col = "churn"                         # Target feature to predict
project_name = "Churn Prediction via API"    # Name of the project
protected_feature = "state"                  # Feature to monitor for fairness/bias
fairness_metric = "equalParity"              # Metric to use for fairness evaluation
preferable_target_value = "yes"              # The favorable outcome for the target

# Create a project from the specified data source
project = dr.Project.create_from_data_source(
    data_source_id=data_source_id,
    credential_id=credential_id,
    project_name=project_name,
    use_case=use_case_id,
)

# Configure advanced options, specifically for bias and fairness
advanced_options = dr.AdvancedOptions(
    protected_features=[protected_feature],
    preferable_target_value=preferable_target_value,
    fairness_metrics_set=fairness_metric
)

# Print the project ID for reference
print(project.id)

# Start the Autopilot process to analyze data and build models
# worker_count=-1 means use all available workers
project.analyze_and_model(
    advanced_options=advanced_options,
    target=target_col,
    worker_count=-1,
)

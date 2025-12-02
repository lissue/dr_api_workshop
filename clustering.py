import datarobot as dr

# Initialize the DataRobot client
dr.Client()

# Configuration parameters
use_case_id = "68f8035c957e8e82f4cc1b1f"    # Use Case ID to associate with the project
project_name = "Clustering via API"          # Name for the new project
data_source_id = "64c12903d08274d3bd214806"  # ID of the data source
credential_id = "64c11792ed57dee5c1ed9cc0"   # Credentials for the data source

# Create a project using the existing data source
project = dr.Project.create_from_data_source(
    data_source_id=data_source_id,
    credential_id=credential_id,
    project_name=project_name,
    use_case=use_case_id,
)

# Print the project ID
print(project.id)

# Start the modeling process for unsupervised clustering
# This specifies unsupervised mode and sets the desired number of clusters
project.analyze_and_model(
    mode='comprehensive',          # Run a comprehensive Autopilot
    unsupervised_mode=True,        # Enable unsupervised learning
    unsupervised_type="clustering",# Specific unsupervised type
    autopilot_cluster_list=[10],   # Request 10 clusters
    worker_count=-1,               # Use max available workers
)
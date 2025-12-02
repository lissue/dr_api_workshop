import datarobot as dr

dr.Client()

use_case_id = "68f8035c957e8e82f4cc1b1f"
project_name = "Clustering via API"
data_source_id = "64c12903d08274d3bd214806"
credential_id = "64c11792ed57dee5c1ed9cc0"

project = dr.Project.create_from_data_source(
    data_source_id=data_source_id,
    credential_id=credential_id,
    project_name=project_name,
    use_case=use_case_id,
)
print(project.id)
project.analyze_and_model(
    mode='comprehensive',
    unsupervised_mode=True,
    unsupervised_type="clustering",
    autopilot_cluster_list=[10],
    worker_count=-1,
)
import datarobot as dr

dr.Client()

use_case_id = "68f8035c957e8e82f4cc1b1f"

for ds in dr.DataSource.list():
    if 'fraud' in ds.canonical_name.lower():
        print(ds.id, ds.canonical_name)
    if 'churn' in ds.canonical_name.lower():
        print(ds.id, ds.canonical_name)
    if 'lending' in ds.canonical_name.lower():
        print(ds.id, ds.canonical_name)

data_source_id = "64c12903d08274d3bd214806"
credential_id = "64c11792ed57dee5c1ed9cc0"
target_col = "churn"
project_name = "Churn Prediction via API"
protected_feature = "state"
fairness_metric = "equalParity"
preferable_target_value = "yes"

project = dr.Project.create_from_data_source(
    data_source_id=data_source_id,
    credential_id=credential_id,
    project_name=project_name,
    use_case=use_case_id,
)
advanced_options = dr.AdvancedOptions(
    protected_features=[protected_feature],
    preferable_target_value=preferable_target_value,
    fairness_metrics_set=fairness_metric
)
print(project.id)
project.analyze_and_model(
    advanced_options=advanced_options,
    target=target_col,
    worker_count=-1,
)

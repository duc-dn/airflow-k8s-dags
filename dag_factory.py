# import pathlib
#
# import dagfactory
# from dagfactory import DagFactory
#
# path = pathlib.Path(__file__).parent.resolve()
# print(f"{path}/dag.yaml")
# dag_factory: DagFactory = dagfactory.DagFactory(f"{path}/dag.yaml")
#
# dag_factory.clean_dags(globals())
# dag_factory.generate_dags(globals())

# dags = dag_factory.build_dags()
# print(dags["example_dag1"])

# 'airflow' word is required for the dagbag to parse this file
from dagfactory import load_yaml_dags

load_yaml_dags(globals_dict=globals(), suffix=['dag.yaml'])

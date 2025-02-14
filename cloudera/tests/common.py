import os
from collections import defaultdict

from datadog_checks.cloudera.metrics import NATIVE_METRICS, TIMESERIES_METRICS
from datadog_checks.dev import get_docker_hostname, get_here

HOST = get_docker_hostname()
PORT = 7180

INSTANCE = {
    'api_url': 'http://localhost:8080/api/v48/',
    'tags': ['test1'],
}

INIT_CONFIG = {
    'workload_username': '~',
    'workload_password': '~',
}

HERE = get_here()
COMPOSE_FILE = os.path.join(HERE, 'docker', 'docker-compose.yaml')

CAN_CONNECT_TAGS = [
    'api_url=http://localhost:8080/api/v48/',
    'test1',
]
CLUSTER_HEALTH_TAGS = [
    '_cldr_cb_clustertype:Data Hub',
    '_cldr_cb_origin:cloudbreak',
    'cloudera_cluster:cod--qfdcinkqrzw',
    'test1',
]


def merge_dicts(d1, d2):
    merged_dict = defaultdict(list)
    for d in (d1, d2):
        for key, value in d.items():
            merged_dict[key] += value
    return merged_dict


METRICS = merge_dicts(NATIVE_METRICS, TIMESERIES_METRICS)

# (C) Datadog, Inc. 2010-2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
import pytest

from .common import (
    CHECK_NAME,
    MINIMAL_INSTANCE,
)
from datadog_checks.active_directory import ActiveDirectoryCheck
from datadog_checks.active_directory.active_directory import DEFAULT_COUNTERS

from datadog_test_libs.win.pdh_mocks import pdh_mocks_fixture, initialize_pdh_tests  # noqa: F401


@pytest.mark.usefixtures('pdh_mocks_fixture')
def test_basic_check(aggregator):
    initialize_pdh_tests()
    instance = MINIMAL_INSTANCE
    c = ActiveDirectoryCheck(CHECK_NAME, {}, {}, [instance])
    c.check(instance)

    for metric_def in DEFAULT_COUNTERS:
        metric = metric_def[3]
        aggregator.assert_metric(metric, tags=None, count=1)

    assert aggregator.metrics_asserted_pct == 100.0

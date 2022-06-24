import os

import pytest

from tests.authenication.login.common.advisor_owner import AdvisorOwnerLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "one_edu", reason="The Class belongs to client one education")
class TestOneEduAdvisorOwnerLoginClass(AdvisorOwnerLoginClass):
    pass

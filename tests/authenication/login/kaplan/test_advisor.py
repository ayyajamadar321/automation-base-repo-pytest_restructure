import os

import pytest

from tests.authenication.login.common.advisor_owner import AdvisorOwnerLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "kaplan", reason="The Class belongs to client kaplan")
class TestKaplanAdvisorOwnerLoginClass(AdvisorOwnerLoginClass):
    pass

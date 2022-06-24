import os

import pytest

from tests.authenication.login.common.division_owner import DivisionOwnerLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "kaplan", reason="The Class belongs to client kaplan")
class TestKaplanDivisionOwnerLoginClass(DivisionOwnerLoginClass):
    pass

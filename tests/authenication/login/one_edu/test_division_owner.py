import os

import pytest

from tests.authenication.login.common.division_owner import DivisionOwnerLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "one_edu", reason="The Class belongs to client one education")
class TestOneEduDivisionOwnerLoginClass(DivisionOwnerLoginClass):
    pass

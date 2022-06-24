import os

import pytest

from tests.authenication.login.common.account_owner import AccountOwnerLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "one_edu", reason="The Class belongs to client one education")
class TestOneEduAccountOwnerLoginClass(AccountOwnerLoginClass):
    pass

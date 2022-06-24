import os

import pytest

from tests.authenication.login.common.account_owner import AccountOwnerLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "kaplan", reason="The Class belongs to client kaplan")
class TestKaplanAccountOwnerLoginClass(AccountOwnerLoginClass):
    pass

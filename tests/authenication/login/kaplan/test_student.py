import os

import pytest

from tests.authenication.login.common.student import StudentLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "kaplan", reason="The Class belongs to client kaplan")
class TestKaplanStudentLoginClass(StudentLoginClass):
    pass

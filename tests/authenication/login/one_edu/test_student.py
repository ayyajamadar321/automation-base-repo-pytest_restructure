import os

import pytest

from tests.authenication.login.common.student import StudentLoginClass


@pytest.mark.skipif(os.getenv("CLIENT") != "one_edu", reason="The Class belongs to client one education")
class TestOneEduStudentLoginClass(StudentLoginClass):
    pass

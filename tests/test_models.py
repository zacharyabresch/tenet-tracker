from freezegun import freeze_time
from datetime import datetime
from uuid import UUID
from tenet_tracker.models import uuid_factory, now_factory, Tenet, Achievement


def is_valid_uuid(test_uuid):
    try:
        UUID(test_uuid)
        return True
    except ValueError:
        return False


def test_uuid_factory():
    assert is_valid_uuid(uuid_factory())


@freeze_time("2020-07-10")
def test_now_factory():
    assert datetime.now().isoformat() == now_factory()


class TestTenet:
    def setup_method(self, method):
        # print(f"\nsetting up: {method=}")
        self.tenet = Tenet(description="Test description", frequency=1, days=1)

    def teardown_method(self, method):
        # print(f"\ntearing down: {method=}")
        pass

    def test_is_tenet(self):
        assert type(self.tenet) == Tenet


class TestAchievement:
    def setup_method(self, method):
        # print(f"\nsetting up: {method=}")
        self.tenet = Tenet(description="Test description", frequency=1, days=1)
        self.achievement = Achievement(tenet_id=self.tenet.id)

    def teardown_method(self, method):
        # print(f"\ntearing down: {method=}")
        pass

    def test_is_achievement(self):
        assert type(self.achievement) == Achievement
